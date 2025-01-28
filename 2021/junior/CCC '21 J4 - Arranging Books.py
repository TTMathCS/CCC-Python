s = input()
l, m, n = s.count("L"), s.count("M"), len(s)

# Segments
seg_l, seg_m, seg_s = s[:l], s[l:l + m], s[l + m:]

# Misplaced counts
mis_l = {"M": seg_l.count("M"), "S": seg_l.count("S")}
mis_m = {"L": seg_m.count("L"), "S": seg_m.count("S")}
mis_s = {"L": seg_s.count("L"), "M": seg_s.count("M")}

# Swaps
swaps = 0

# Direct swaps: L <-> M, L <-> S, M <-> S
lm = min(mis_l["M"], mis_m["L"])
swaps += lm
mis_l["M"] -= lm
mis_m["L"] -= lm

ls = min(mis_l["S"], mis_s["L"])
swaps += ls
mis_l["S"] -= ls
mis_s["L"] -= ls

ms = min(mis_m["S"], mis_s["M"])
swaps += ms
mis_m["S"] -= ms
mis_s["M"] -= ms

# Circular swaps
swaps += 2 * sum(mis_l.values())

print(swaps)
