import sys
from collections import deque

ROWS = int(input())
COLS = int(input())
end = ROWS * COLS
graph = [[] for _ in range(end + 1)]

# constructing the graph
for r in range(1, ROWS + 1):
    row = map(int, input().split())
    c = 1
    for num in row:
        if num <= end:
            graph[r * c].append(num)  # avoid having to factor
        c += 1

# simple BFS on adjacency list
visited = [False for _ in range(end + 1)]
visited[1] = True
q = deque([1])

while q:
    current = q.popleft()

    if current == end:
        print("yes")
        sys.exit()  # end code

    for adj in graph[current]:
        if not visited[adj]:
            visited[adj] = True
            q.append(adj)

print("no")
