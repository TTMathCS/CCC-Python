r = int(input())
c = int(input())
m = []
for _ in range(r):
    m.append(list(input()))

i = int(input())
j = int(input())

total = 0
q = [(i, j)]
visited = set()

while q:
    x, y = q.pop(0)
    if (x, y) in visited or x < 0 or x >= r or y < 0 or y >= c or m[x][y] == '*' or m[x][y] == '-':
        continue

    visited.add((x, y))

    if m[x][y] == 'S':
        total += 1
    elif m[x][y] == 'M':
        total += 5
    elif m[x][y] == 'L':
        total += 10

    m[x][y] = '-'  # mark as visited

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        q.append((x + dx, y + dy))

print(total)
