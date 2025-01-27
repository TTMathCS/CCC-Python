n = int(input())
s = [0 for _ in range(5)]
for i in range(n):
    inp = input()
    for j in range(5):
        if inp[j] == "Y": s[j] += 1
m = max(s)
o = ""
for i in range(5):
    if s[i] == m:
        o = o + str(i + 1) + ","
print(o[:-1])
