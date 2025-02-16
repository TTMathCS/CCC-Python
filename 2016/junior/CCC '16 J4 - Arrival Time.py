## https://dmoj.ca/problem/ccc16j4
# solution 1 is brute force, list all possibility in a dictonary

def time_to_minutes(t) -> int:
    # t is HH:MM format
    h, m = map(int, t.split(":"))
    return h * 60 + m


def minutes_to_time(minutes) -> str:
    # convert minutes back to "HH:MM" format
    h = minutes // 60 % 24
    m = minutes % 60
    return f"{h:02}:{m:02}"


minutes = time_to_minutes(input())

# out of 5-10 and 13-19
if not (300 < minutes < 600 or 780 < minutes < 1140):
    minutes += 120
elif 300 < minutes < 420:
    mins_before_rush = max(0, 420 - minutes)
    mins_during_rush = min((120 - mins_before_rush) * 2, 180)
    mins_after_rush = 120 - mins_before_rush - mins_during_rush // 2
    minutes += mins_before_rush + mins_during_rush + mins_after_rush
elif 420 <= minutes < 600:
    mins_after_rush = 120 - (180 - (minutes - 420)) // 2
    minutes = 600 + mins_after_rush
elif 780 < minutes < 900:
    mins_before_rush = max(0, 900 - minutes)
    mins_during_rush = min((120 - mins_before_rush) * 2, 240)
    mins_after_rush = 120 - mins_before_rush - mins_during_rush // 2
    minutes += mins_before_rush + mins_during_rush + mins_after_rush
elif 900 <= minutes < 1140:
    mins_after_rush = 120 - (240 - (minutes - 900)) // 2
    minutes = 1140 + mins_after_rush

print(minutes_to_time(minutes))
