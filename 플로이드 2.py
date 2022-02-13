import sys

import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

map_ = [[INF] * (N+1) for _ in range(N+1)]
for i in range(N+1):
    map_[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    map_[a][b] = min(map_[a][b], c)

path = []

for i in range(N+1):
    path.append([])

    for j in range(N+1):
        path[-1].append([str(i), str(j)])

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if map_[i][k] + map_[k][j] < map_[i][j]:
                map_[i][j] = map_[i][k] + map_[k][j]

                path[i][j] = path[i][k] + path[k][j][1:]

for i in range(1, N+1):
    for j in range(1, N+1):
        if map_[i][j] == INF: print(0, end=" ")
        else: print(map_[i][j], end=" ")
    print()

for i in range(1, N+1):
    for j in range(1, N+1):
        if map_[i][j] == INF or i == j: print(0)
        else: print(len(path[i][j]), " ".join(path[i][j]))