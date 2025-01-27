# from collections import defaultdict

# N = int(input())
# d = defaultdict(lambda: 0)

# for _ in range(N):
#     number = int(input())
#     d[number] += 1

# score = list(d.keys())
# score.sort(reverse=True)
# print(score[2], d[score[2]])


# method 2

N = int(input())
lst = [int(input()) for _ in range(N)]
uniq = []
for v in lst:
    if v not in uniq:
        uniq.append(v)
uniq.sort(reverse=True)
broze = uniq[2]

num = 0
for i in lst:
    if i == broze:
        num += 1

print(broze, num)




