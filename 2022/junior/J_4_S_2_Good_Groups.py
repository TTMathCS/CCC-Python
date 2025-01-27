f = int(input())
friends, enemies = {}, {}

for _ in range(f):
    a, b = input().split()
    friends.setdefault(a, set()).add(b)
    friends.setdefault(b, set()).add(a)

e = int(input())
for _ in range(e):
    a, b = input().split()
    enemies.setdefault(a, set()).add(b)
    enemies.setdefault(b, set()).add(a)

g = int(input())
f_set, e_set = set(), set()

for _ in range(g):
    group = set(input().split())
    for person in group:
        if person in friends:
            f_set.update((person, friend) for friend in friends[person] if friend not in group)
        if person in enemies:
            e_set.update((person, enemy) for enemy in enemies[person] if enemy in group)

print((len(f_set) + len(e_set)) // 2)
