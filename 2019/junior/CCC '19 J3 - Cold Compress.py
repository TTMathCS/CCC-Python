n = int(input())
for _ in range(n):
    s = input()
    lst, count = [], 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            lst.append(f"{count} {s[i - 1]}")
            count = 1
        else:
            count += 1
    lst.append(f"{count} {s[-1]}")
    print(" ".join(lst))
