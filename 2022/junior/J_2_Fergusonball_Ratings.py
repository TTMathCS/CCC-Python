n = int(input())
total = sum(1 for _ in range(n) if int(input()) * 5 - int(input()) * 3 > 40)
print(f"{total}{'+' if total == n else ''}")
