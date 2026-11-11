#!/usr/bin/env python3
"""Astronomical helper for the astrological-spiritual-healer skill.

Computes real Sun/Moon longitudes (Meeus low-precision series: Moon ~0.3 deg,
Sun ~0.01 deg), the Sun-Moon elongation and lunar phase, the Ascendant and
Midheaven, and the mean lunar node. No third-party packages required.

Usage:
  python astro_calc.py moon-now  --utc 2026-11-11T22:50
  python astro_calc.py natal     --date 1982-11-15 --time 18:20 --tz 1 --lat 6.37 --lon 2.43
  python astro_calc.py natal     --date 1985-12-08            # no time: Moon sign range + ingress

--tz is the offset of local time from UTC in hours (Benin = 1). --lon is east-positive.
"""
import argparse
import datetime as dt
import json
import math

SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra",
         "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
SYNODIC = 29.530588853
PHASES = [  # (upper bound in days, name) - same bands as SKILL.md Step 4
    (1.85, "New Moon"), (7.38, "Waxing Crescent"), (11.07, "First Quarter"),
    (14.77, "Waxing Gibbous"), (16.61, "Full Moon"), (22.15, "Waning Gibbous"),
    (25.84, "Last Quarter"), (SYNODIC + 1, "Waning Crescent"),
]
rad = math.radians


def norm(x):
    return x % 360.0


def julian_day(t):
    y, m = t.year, t.month
    d = t.day + (t.hour + (t.minute + t.second / 60) / 60) / 24
    if m <= 2:
        y, m = y - 1, m + 12
    a = y // 100
    b = 2 - a + a // 4
    return int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + d + b - 1524.5


def moon_lon(jd):
    t = (jd - 2451545.0) / 36525
    lp = norm(218.3164477 + 481267.88123421 * t)
    d = norm(297.8501921 + 445267.1114034 * t)
    m = norm(357.5291092 + 35999.0502909 * t)
    mp = norm(134.9633964 + 477198.8675055 * t)
    f = norm(93.2720950 + 483202.0175233 * t)
    s = math.sin
    return norm(lp + 6.288774 * s(rad(mp)) + 1.274027 * s(rad(2 * d - mp))
                + 0.658314 * s(rad(2 * d)) + 0.213618 * s(rad(2 * mp))
                - 0.185116 * s(rad(m)) - 0.114332 * s(rad(2 * f))
                + 0.058793 * s(rad(2 * d - 2 * mp)) + 0.057066 * s(rad(2 * d - m - mp))
                + 0.053322 * s(rad(2 * d + mp)) + 0.045758 * s(rad(2 * d - m))
                - 0.040923 * s(rad(m - mp)) - 0.034720 * s(rad(d))
                - 0.030383 * s(rad(m + mp)))


def sun_lon(jd):
    t = (jd - 2451545.0) / 36525
    l0 = norm(280.46646 + 36000.76983 * t)
    m = norm(357.52911 + 35999.05029 * t)
    c = ((1.914602 - 0.004817 * t) * math.sin(rad(m))
         + 0.019993 * math.sin(rad(2 * m)))
    return norm(l0 + c)


def mean_node(jd):
    t = (jd - 2451545.0) / 36525
    return norm(125.04452 - 1934.136261 * t)


def elongation(jd):
    return norm(moon_lon(jd) - sun_lon(jd))


def angles(jd, lat, lon_east):
    """Ascendant and Midheaven (tropical, longitudes in degrees)."""
    t = (jd - 2451545.0) / 36525
    gmst = norm(280.46061837 + 360.98564736629 * (jd - 2451545.0))
    ramc = rad(norm(gmst + lon_east))
    eps = rad(23.4392911 - 0.0130042 * t)
    phi = rad(lat)
    asc = math.degrees(math.atan2(
        math.cos(ramc),
        -(math.sin(ramc) * math.cos(eps) + math.tan(phi) * math.sin(eps))))
    mc = math.degrees(math.atan2(math.sin(ramc), math.cos(ramc) * math.cos(eps)))
    return norm(asc), norm(mc)


def fmt(lon):
    return f"{SIGNS[int(lon // 30)]} {lon % 30:.1f}\u00b0"


def phase_info(jd):
    e = elongation(jd)
    day = e / 360 * SYNODIC
    name = next(n for bound, n in PHASES if day < bound)
    return e, day, name


def last_new_moon(jd):
    """Bisect for the most recent exact conjunction before jd."""
    e = elongation(jd)
    lo = jd - e / 360 * SYNODIC - 1.5  # safely before the conjunction
    hi = jd - e / 360 * SYNODIC + 1.5
    for _ in range(50):
        mid = (lo + hi) / 2
        diff = (elongation(mid) + 180) % 360 - 180  # signed, 0 at conjunction
        if diff < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def jd_to_dt(jd):
    return dt.datetime(2000, 1, 1, 12) + dt.timedelta(days=jd - 2451545.0)


def moon_now(utc):
    jd = julian_day(utc)
    e, day, name = phase_info(jd)
    nm = last_new_moon(jd)
    return {
        "utc": utc.isoformat(timespec="minutes"),
        "sun": fmt(sun_lon(jd)), "moon": fmt(moon_lon(jd)),
        "elongation_deg": round(e, 1), "phase_day": round(day, 2),
        "phase": name, "illumination_pct": round((1 - math.cos(rad(e))) / 2 * 100),
        "last_new_moon_utc": jd_to_dt(nm).isoformat(timespec="minutes"),
        "days_since_new_moon": round(jd - nm, 2),
    }


def natal(date, time, tz, lat, lon):
    out = {"date": date.isoformat()}
    if time is not None:
        utc = dt.datetime.combine(date, time) - dt.timedelta(hours=tz)
        jd = julian_day(utc)
        e, day, name = phase_info(jd)
        out.update({
            "utc": utc.isoformat(timespec="minutes"),
            "sun": fmt(sun_lon(jd)), "moon": fmt(moon_lon(jd)),
            "birth_lunation": name, "elongation_deg": round(e, 1),
            "north_node_mean": fmt(mean_node(jd)),
            "south_node_mean": fmt(norm(mean_node(jd) + 180)),
        })
        if lat is not None and lon is not None:
            asc, mc = angles(jd, lat, lon)
            out.update({"ascendant": fmt(asc), "midheaven": fmt(mc)})
    else:
        # No time: report the Moon across the day (00:00-24:00 UT) and any ingress.
        start = julian_day(dt.datetime.combine(date, dt.time()))
        first, last = moon_lon(start), moon_lon(start + 1)
        out.update({"sun_at_noon_ut": fmt(sun_lon(start + 0.5)),
                    "moon_00h_ut": fmt(first), "moon_24h_ut": fmt(last),
                    "north_node_mean": fmt(mean_node(start + 0.5))})
        if int(first // 30) != int(last // 30):
            target = (int(last // 30)) * 30
            lo, hi = start, start + 1
            for _ in range(40):
                mid = (lo + hi) / 2
                if (moon_lon(mid) - target + 180) % 360 - 180 < 0:
                    lo = mid
                else:
                    hi = mid
            out["moon_ingress_utc"] = (
                f"{SIGNS[int(last // 30)]} at {jd_to_dt((lo + hi) / 2).strftime('%H:%M')} UT")
        else:
            out["moon_sign_certain"] = SIGNS[int(first // 30)]
        e, day, name = phase_info(start + 0.5)
        out["birth_lunation_approx"] = name
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("moon-now")
    a.add_argument("--utc", help="ISO UTC datetime; default = now")
    b = sub.add_parser("natal")
    b.add_argument("--date", required=True)
    b.add_argument("--time")
    b.add_argument("--tz", type=float, default=0.0)
    b.add_argument("--lat", type=float)
    b.add_argument("--lon", type=float)
    args = p.parse_args()
    if args.cmd == "moon-now":
        utc = dt.datetime.fromisoformat(args.utc) if args.utc else dt.datetime.utcnow()
        print(json.dumps(moon_now(utc), indent=2))
    else:
        t = dt.time.fromisoformat(args.time) if args.time else None
        print(json.dumps(natal(dt.date.fromisoformat(args.date), t, args.tz, args.lat, args.lon), indent=2))


if __name__ == "__main__":
    main()
