import math

p, n, r = [int(input()) for _ in range(3)]
d = p / n - 1 if r == 1 else math.log((p * (r - 1) / n + 1), r) - 1
print(int(d) + 1)
