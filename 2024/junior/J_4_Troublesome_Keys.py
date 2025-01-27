# forloops
# fxrlxxps
# There must be silly key but not necessary quite key
# solution 1 thought:
# in s1 but not in s2: silly key or quite key
# in s2 but not in s1: must be silly key

s1_silly_or_quite_key = ""
s2_silly = ""

s1 = input()
s2 = input()
for c in s2:
    if c not in s1: s2_silly = c

for c in s1:
    if c not in s2 and c not in s1_silly_or_quite_key: s1_silly_or_quite_key += c

# print(s1_silly_or_quite_key)
# print(s2_silly)

if len(s1_silly_or_quite_key) == 1: # no quite key
    print(s1_silly_or_quite_key,s2_silly)
    print("-")
else:
    if s1.replace(s1_silly_or_quite_key[0], s2_silly).replace(s1_silly_or_quite_key[1], "") == s2:
        print(s1_silly_or_quite_key[0], s2_silly)
        print(s1_silly_or_quite_key[1])
    else:
        print(s1_silly_or_quite_key[1], s2_silly)
        print(s1_silly_or_quite_key[0])

