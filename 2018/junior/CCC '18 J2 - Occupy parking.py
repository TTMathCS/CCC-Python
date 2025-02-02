n, s1, s2 = int(input()), input(), input()
print(sum([1 for i in range(n) if s1[i] == s2[i] == "C"]))
