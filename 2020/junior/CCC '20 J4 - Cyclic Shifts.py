t, s = input(), input()
print("yes" if any((s := s[1:] + s[0]) in t for _ in s) else "no")
