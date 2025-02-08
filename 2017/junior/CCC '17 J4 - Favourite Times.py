m = int(input())
seq = [34,
       71, 83, 95, 107, 119,
       130, 144, 154, 166, 178,
       201, 213, 225, 237,
       260, 272, 284, 296,
       331, 343, 355,
       390, 402, 414,
       461, 473,
       520, 532,
       591,
       672]

cycles, remainder = divmod(m, 720)
num = next((i for i, time in enumerate(seq) if remainder < time), len(seq))
print(num + cycles * len(seq))
