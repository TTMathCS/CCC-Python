def solve():
    def t2m(t):
        # Convert time from HH:MM format to minutes since midnight (00:00)
        # Example: "7:30" -> 7*60 + 30 = 450 minutes
        return sum(int(x) * y for x, y in zip(t.split(':'), [60, 1]))

    def m2t(m):
        # Convert minutes since midnight back to HH:MM format
        # Example: 450 -> "07:30"
        # Uses % 24 to handle times past midnight and :02d for padding with zeros
        return f"{m // 60 % 24:02d}:{m % 60:02d}"

    # Read departure time from input
    m = t2m(input())

    # If not during rush hours (5:00-10:00 or 13:00-19:00), simply add 2 hours (120 minutes)
    if not (300 < m < 600 or 780 < m < 1140):
        print(m2t(m + 120))
        return

    # Rush Hour Details:
    # Morning rush: 5:00-10:00 (300-600 minutes)
    # Evening rush: 13:00-19:00 (780-1140 minutes)
    # Peak periods:
    # - Morning peak: 7:00-9:00 (420-540 minutes) - worst case adds 3 hours
    # - Evening peak: 15:00-17:00 (900-1020 minutes) - worst case adds 4 hours

    # Handle morning rush hour (5:00-10:00)
    if 300 < m < 600:
        if m < 420:  # Before morning peak
            pre = max(0, 420 - m)  # Normal travel time before peak
            rush = min((120 - pre) * 2, 180)  # Double time during peak period
            post = 120 - pre - rush // 2  # Normal travel time after peak
            m += pre + rush + post
        else:  # During or after morning peak
            # Calculate remaining time considering already spent time in peak
            m = 600 + 120 - (180 - (m - 420)) // 2

    # Handle evening rush hour (13:00-19:00)
    else:
        if m < 900:  # Before evening peak
            pre = max(0, 900 - m)  # Normal travel time before peak
            rush = min((120 - pre) * 2, 240)  # Double time during peak period
            post = 120 - pre - rush // 2  # Normal travel time after peak
            m += pre + rush + post
        else:  # During or after evening peak
            # Calculate remaining time considering already spent time in peak
            m = 1140 + 120 - (240 - (m - 900)) // 2

    # Print final arrival time
    print(m2t(m))


solve()
