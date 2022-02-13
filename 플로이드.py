import sys
input = sys.stdin.readline

INF = sys.maxsize

N = int(input())
M = int(input())

cost_data = [[INF] * (N+1) for _ in range(N+1)] # cost_data[a][b] = a에서 b로 가는 비용
for i in range(N+1):
    cost_data[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    cost_data[a][b] = min(cost_data[a][b], c)

for k in range(1, N+1): # k = 거쳐가야 하는 정점
    for i in range(1, N+1):
        for j in range(1, N+1):
            i2k2j = cost_data[i][k] + cost_data[k][j]
            if i2k2j < cost_data[i][j]:
                cost_data[i][j] = i2k2j

for i in range(1, N+1):
    for j in range(1, N+1):
        if cost_data[i][j] == sys.maxsize: print(0, end=" ")
        else: print(cost_data[i][j], end=" ")
    print()