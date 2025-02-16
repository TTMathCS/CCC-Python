m, d = int(input()), int(input())
print("Before" if m == 1 or (m == 2 and d < 18) else "Special" if m == 2 and d == 18 else "After")
