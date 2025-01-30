from collections import defaultdict

# Input
m, n, k = int(input()), int(input()), int(input())
row_counts, col_counts = defaultdict(int), defaultdict(int)

# Record the toggles
for _ in range(k):
    x, y = input().split()
    y = int(y)
    if x == 'R':
        row_counts[y] += 1
    else:
        col_counts[y] += 1

# Count rows and columns toggled an odd number of times
odd_rows = sum(1 for count in row_counts.values() if count % 2 == 1)
odd_cols = sum(1 for count in col_counts.values() if count % 2 == 1)

# Total painted cells
total = odd_rows * n + odd_cols * m - 2 * odd_rows * odd_cols

print(total)
