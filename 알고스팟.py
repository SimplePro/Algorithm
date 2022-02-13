import heapq
import sys
INF = sys.maxsize

M, N = map(int, input().split())

map_ = []
for _ in range(N):
    map_.append([])
    for i in input():
        map_[-1].append(int(i))

break_data = [[INF] * M for _ in range(N)]
break_data[0][0] = 0

heap = []
heapq.heappush(heap, (0, (0, 0)))

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

while heap:
    break_, (i, j) = heapq.heappop(heap)

    if break_data[i][j] < break_: continue

    for k in range(4):
        next_i, next_j = i+di[k], j+dj[k]

        if 0 <= next_i < N and 0 <= next_j < M and map_[next_i][next_j] + break_ < break_data[next_i][next_j]:
            break_data[next_i][next_j] = map_[next_i][next_j] + break_
            heapq.heappush(heap, (break_data[next_i][next_j], (next_i, next_j)))

print(break_data[N-1][M-1])