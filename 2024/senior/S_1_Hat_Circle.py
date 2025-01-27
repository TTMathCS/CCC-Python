N = int(input())
s = 0
lst = []
for i in range(N):
    lst.append(int(input()))
for i in range(N//2):
    if lst[i] == lst[i+N//2]:
        s += 1
print(2*s)
