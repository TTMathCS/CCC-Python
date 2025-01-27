n = int(input())
r1 = list(map(int, input().split(" ")))
r2 = list(map(int, input().split(" ")))
s = 0
for i in range(n):
    if r1[i] == 1:
        s += 3
    if i > 0 and r1[i - 1] == r1[i] == 1: # first row if adjacent
        s -= 2
    if r2[i] == 1:
        s += 3
    if i > 0 and r2[i - 1] == r2[i] == 1: # second row if adjacent
        s -= 2
    if i % 2 == 0 and r1[i] == r2[i] == 1: # top-bottom over count
        s -= 2
print(s)
