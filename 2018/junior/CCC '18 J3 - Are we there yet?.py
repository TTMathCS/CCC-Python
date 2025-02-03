lst = list(map(int, input().split()))
psa = [0]
for i in lst:
    psa.append(psa[-1] + i)

for i in range(5):
    new_lst = [abs(j - psa[i]) for j in psa]
    print(" ".join(map(str, new_lst)))
