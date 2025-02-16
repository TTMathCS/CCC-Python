happy = ":-)"
sad = ":-("
s = input()
print("none" if s.count(happy) == s.count(sad) == 0 else "unsure" if s.count(happy) == s.count(
    sad) else "happy" if s.count(happy) > s.count(sad) else "sad")
