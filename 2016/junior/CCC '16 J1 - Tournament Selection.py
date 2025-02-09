wins = sum(input() == 'W' for _ in range(6))
print(-1 if wins == 0 else 3 if wins < 3 else 2 if wins < 5 else 1)
