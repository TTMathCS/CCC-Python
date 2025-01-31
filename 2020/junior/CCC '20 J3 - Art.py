# method 1: it is more efficient than method 2
# n = int(input())
# x0, y0, x1, y1 = (101, 101, -1, -1)
# for _ in range(n):
#     x, y = map(int, input().split(","))
#     x0 = x if x < x0 else x0
#     x1 = x if x > x1 else x1
#     y0 = y if y < y0 else y0
#     y1 = y if y > y1 else y1
# print(f"{x0 - 1},{y0 - 1}")
# print(f"{x1 + 1},{y1 + 1}")

# method 2:
n = int(input())
points = [tuple(map(int, input().split(","))) for _ in range(n)]

x_coords, y_coords = zip(*points)
x0, x1 = min(x_coords), max(x_coords)
y0, y1 = min(y_coords), max(y_coords)

print(f"{x0 - 1},{y0 - 1}")
print(f"{x1 + 1},{y1 + 1}")
