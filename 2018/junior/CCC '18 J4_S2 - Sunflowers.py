def is_valid(grid):
    for i in range(n):
        for j in range(1, n):
            if grid[i][j] < grid[i][j - 1] or grid[j][i] < grid[j - 1][i]:
                return False
    return True


def rotate_right(grid):
    lst = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(grid[n - j - 1][i])
        lst.append(row)
    return lst


def print_grid(grid):
    for i in range(n):
        print(" ".join(map(str, grid[i])))


n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))


for _ in range(4):
    grid = rotate_right(grid)
    if is_valid(grid):
        print_grid(grid)
        break
