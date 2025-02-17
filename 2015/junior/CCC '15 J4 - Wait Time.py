from collections import defaultdict as dd

n = int(input())
d = dd(lambda: (-1, 0))
t = 0
for _ in range(n):
    a, b = input().split()
    if a == "W": t += int(b) - 1;continue
    b = int(b)
    s, w = d[b]
    if a == "R":
        d[b] = (t, w)
    else:
        d[b] = (-1, w + t - s)
    t += 1
for k in sorted(d):
    s, w = d[k]
    print(k, "-1" if s != -1 else w)
