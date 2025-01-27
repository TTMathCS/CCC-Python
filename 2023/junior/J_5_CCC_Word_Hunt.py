# Input
s = input().strip()
r, c = int(input()), int(input())
g = [input().split() for _ in range(r)]

# Directions. index is used to calculate perpendicular angles
d = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

# BFS Implementation
res = 0
for i in range(r):
    for j in range(c):
        if g[i][j] == s[0]:
            q = [(i, j, s[0], -1, 0)]  # (x, y, formed word, dir, turns)
            while q:
                x, y, w, prev_d, t = q.pop(0)
                if w == s:
                    res += 1
                    continue
                nxt = s[len(w)]
                for nd, (dx, dy) in enumerate(d):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c and g[nx][ny] == nxt:
                        if prev_d == -1 or prev_d == nd:
                            if t < 2: q.append((nx, ny, w + nxt, nd, t))
                        elif t < 1 and abs(prev_d - nd) in (2, 6):
                            q.append((nx, ny, w + nxt, nd, t + 1))

# Output
print(res)
