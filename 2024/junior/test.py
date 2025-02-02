n = int(input())
d1, d2, d3, d4, d5 = [], [], [], [], []
for _ in range(n):
    s = input()
    d1.append(s[0])
    d2.append(s[1])
    d3.append(s[2])
    d4.append(s[3])
    d5.append(s[4])
d1_number_of_Y = d1.count("Y")
d2_number_of_Y = d2.count("Y")
d3_number_of_Y = d3.count("Y")
d4_number_of_Y = d4.count("Y")
d5_number_of_Y = d5.count("Y")
max_num = max(d1_number_of_Y, d2_number_of_Y, d3_number_of_Y, d4_number_of_Y, d5_number_of_Y)
days_lst = []
if max_num == d1_number_of_Y:
    days_lst.append("1")
if max_num == d2_number_of_Y:
    days_lst.append("2")
if max_num == d3_number_of_Y:
    days_lst.append("3")
if max_num == d4_number_of_Y:
    days_lst.append("4")
if max_num == d5_number_of_Y:
    days_lst.append("5")
print(",".join(days_lst))
