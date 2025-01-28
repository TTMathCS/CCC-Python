max_bid, winner = 0, ""
for _ in range(int(input())):
    n, b = input(), int(input())
    if b > max_bid:
        max_bid, winner = b, n
print(winner)