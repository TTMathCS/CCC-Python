x1, y1, x2, y2, c = (*map(int, input().split()), *map(int, input().split()), int(input()))
dis = abs(x1 - x2) + abs(y1 - y2)
print("Y" if (c >= dis and (c - dis) % 2 == 0) else "N")
