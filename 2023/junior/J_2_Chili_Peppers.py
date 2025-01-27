n = int(input())
s = 0
for _ in range(n):
    i = input()
    if i == "Poblano":
        s += 1500
    elif i == "Mirasol":
        s += 6000
    elif i == "Serrano":
        s += 15500
    elif i == "Cayenne":
        s += 40000
    elif i == "Thai":
        s += 75000
    else:
        s += 125000
print(s)
