lst = [int(input()) for _ in range(4)]
print("ignore" if lst[0] in (8, 9) and lst[-1] in (8, 9) and lst[1] == lst[2] else "answer")
