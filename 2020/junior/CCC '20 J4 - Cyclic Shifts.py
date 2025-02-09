t, s = input(), input()
# cycle s and for each shift decide if it is in t
print("yes" if any((s := s[1:] + s[0]) in t for _ in s) else "no")
