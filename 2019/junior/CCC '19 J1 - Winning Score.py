a, b = [sum(int(input()) * w for w in (3, 2, 1)) for _ in range(2)]
print("A" if a > b else "B" if a < b else "T")
