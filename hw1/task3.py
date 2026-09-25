def portal_clock(seconds: int) -> tuple[int, int, int, int]:
    sec_day = 86400
    sec_hour = 3600
    sec_min = 60

    days, remainder = divmod(seconds, sec_day)
    hours, remainder = divmod(remainder, sec_hour)
    minutes, seconds_end = divmod(remainder, sec_min)
    return (days, hours, minutes, seconds_end)

print(portal_clock(90061))
print(portal_clock(-1))
print(portal_clock(0))
print(portal_clock(-86400))