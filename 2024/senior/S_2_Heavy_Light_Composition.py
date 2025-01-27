from collections import Counter
n,m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(dict(Counter(input())))
print(lst)