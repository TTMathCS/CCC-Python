def flip(action):
    global g
    g = [[g[1][0], g[1][1]], [g[0][0], g[0][1]]] if action == 'H' else [[g[0][1], g[0][0]], [g[1][1], g[1][0]]]


g = [[1, 2], [3, 4]]
for i in input().replace("VV", "").replace("HH", ""):
    flip(i)
print(*g[0])
print(*g[1])
