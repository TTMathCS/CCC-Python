s1, s2 = input(), input()
s1_keys, s2_key = list(set(s1) - set(s2)), (set(s2) - set(s1)).pop()
if len(s1_keys) == 1:
    print(f"{s1_keys[0]} {s2_key}\n-")
else:
    if s1.replace(s1_keys[0], s2_key).replace(s1_keys[1], "") == s2:
        print(f"{s1_keys[0]} {s2_key}\n{s1_keys[1]}")
    else:
        print(f"{s1_keys[1]} {s2_key}\n{s1_keys[0]}")
