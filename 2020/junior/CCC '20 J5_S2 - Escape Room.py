m, n = [int(input()) for i in range(2)]
lst = [list(map(int, input().split())) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
queue = [(0, 0)]
found = False

while queue:
    r, c = queue.pop(0)
    if r == m - 1 and c == n - 1:
        found = True
        break
    if not visited[r][c]:
        visited[r][c] = True

        if m < n:
            for i in range(1, m + 1):
                if lst[r][c] % i == 0:
                    if lst[r][c] // i <= n:
                        queue.append((i - 1, lst[r][c] // i - 1))
        else:
            for i in range(1, n + 1):
                if lst[r][c] % i == 0:
                    if lst[r][c] // i <= m:
                        queue.append((lst[r][c] // i - 1, i - 1))
if found:
    print("yes")
else:
    print("no")
