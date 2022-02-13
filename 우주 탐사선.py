from itertools import permutations
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int, input().split())

map_ = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if map_[i][j] > map_[i][k] + map_[k][j]:
                map_[i][j] = map_[i][k] + map_[k][j]

result = INF

for sequence in map(list, permutations(list((set(range(N)) - set([K]))), N-1)):
    k_sequence = [K] + sequence
    t = 0
    for i in range(N-1):
        t += map_[k_sequence[i]][k_sequence[i+1]]

    result = min(result, t)

print(result)