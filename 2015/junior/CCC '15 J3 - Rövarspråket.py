VOWELS = "aeiou"


def closest_vowel(c):
    """Find the closest vowel."""
    return min(VOWELS, key=lambda v: abs(ord(c) - ord(v)))


def next_consonant(c):
    """Find next consonant."""
    if c == 'z': return 'z'
    nxt = chr(ord(c) + 1)
    while nxt <= 'z' and nxt in VOWELS: nxt = chr(ord(nxt) + 1)
    return nxt


output = ""
for c in input():
    if c in VOWELS:
        output += c
    else:
        output += c + closest_vowel(c) + next_consonant(c)

print(output)
