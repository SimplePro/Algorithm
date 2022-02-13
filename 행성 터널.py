import sys
input = sys.stdin.readline

N = int(input())

planet_data = [[i] + list(map(int, input().split())) for i in range(N)]

planet_data_x = sorted(planet_data, key=lambda x: x[1])
planet_data_y = sorted(planet_data, key=lambda x: x[2])
planet_data_z = sorted(planet_data, key=lambda x: x[3])

edges = []

for i in range(N-1):
    x_edge = (planet_data_x[i+1][1] - planet_data_x[i][1], planet_data_x[i][0], planet_data_x[i+1][0])
    y_edge = (planet_data_y[i+1][2] - planet_data_y[i][2], planet_data_y[i][0], planet_data_y[i+1][0])
    z_edge = (planet_data_z[i+1][3] - planet_data_z[i][3], planet_data_z[i][0], planet_data_z[i+1][0])

    edges.append(x_edge)
    edges.append(y_edge)
    edges.append(z_edge)

edges.sort(key=lambda x: x[0])

root_data = [i for i in range(N+1)]

def find_root(x):
    if root_data[x] != x:
        root_data[x] = find_root(root_data[x])
    
    return root_data[x]

cost = 0

for c, a, b in edges:
    a_root = find_root(a)
    b_root = find_root(b)

    if a_root != b_root:
        cost += c

        if a_root < b_root: root_data[b_root] = a_root
        else: root_data[a_root] = b_root

print(cost)