r, c = int(input()), int(input())
m = [list(input()) for _ in range(r)]
i, j = int(input()), int(input())

q, visited, total = [(i, j)], set(), 0
values = {'S': 1, 'M': 5, 'L': 10}

while q:
    x, y = q.pop(0)
    if (x, y) in visited or not (0 <= x < r and 0 <= y < c) or m[x][y] in {'*', '-'}:
        continue
    visited.add((x, y))
    total += values.get(m[x][y], 0)
    m[x][y] = '-'
    q += [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]

print(total)
