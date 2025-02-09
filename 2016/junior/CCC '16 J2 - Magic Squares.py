grid = [list(map(int, input().split())) for _ in range(4)]
row_sums = set(sum(row) for row in grid)
col_sums = set(sum(col) for col in zip(*grid))
print("magic" if len(row_sums) == len(col_sums) == 1 and next(iter(row_sums)) == next(iter(col_sums)) else "not magic")
