import sys

input = sys.stdin.read

# Read all inputs
q, n, *arr = map(int, input().split())  # `q`: problem type, `n`: size, `arr`: remaining numbers
d, p = sorted(arr[:n]), sorted(arr[n:])  # Split, sort both lists (d = 1st n elements, p = last n elements)

# Calculate and print the result
print(sum(max(d[i], p[i] if q == 1 else p[n - i - 1]) for i in range(n)))
