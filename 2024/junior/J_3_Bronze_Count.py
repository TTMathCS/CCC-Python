from collections import Counter
lst = [int(input()) for _ in range(int(input()))]
scores = sorted(Counter(lst), reverse=True)
print(scores[2], Counter(lst)[scores[2]])
