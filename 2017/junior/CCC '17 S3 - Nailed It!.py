n = int(input())
board_freq = [0] * 2001
height_freq = [0] * 4001

# Count board frequencies
for x in map(int, input().split()):
    board_freq[x] += 1

# Calculate all possible heights
for i in range(1, 2001):
    if not board_freq[i]:
        continue
    height_freq[i * 2] += board_freq[i] // 2
    for j in range(i + 1, 2001):
        if board_freq[j]:
            height_freq[i + j] += min(board_freq[i], board_freq[j])

# Find max frames and count of heights
max_frames = max(height_freq)
count = sum(1 for h in height_freq if h == max_frames)

print(max_frames, count)
