d, s = "", ""
while True:
    a = input()
    if a == "99999":
        break
    if (int(a[0]) + int(a[1])) % 2 == 1:
        d = "left"
    elif ((int(a[0]) + int(a[1])) % 2 == 0) and (int(a[0]) + int(a[1])) != 0:
        d = "right"
    print(d, a[2:])
