def dfs(x, y, w, pd, t):
    global res
    if w == s: res += 1; return
    for nd, (dx, dy) in enumerate(d):
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and g[nx][ny] == s[len(w)]:
            if (pd == -1 or pd == nd) and t < 2:
                dfs(nx, ny, w + s[len(w)], nd, t)
            elif t < 1 and abs(pd - nd) in (2, 6):
                dfs(nx, ny, w + s[len(w)], nd, t + 1)


s = input().strip()
r, c = int(input()), int(input())
g = [input().split() for _ in range(r)]
d = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
res = 0

for i in range(r):
    for j in range(c):
        if g[i][j] == s[0]: dfs(i, j, s[0], -1, 0)

print(res)
