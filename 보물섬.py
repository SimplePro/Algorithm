import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

map_ = []
all_land_idx = []

for i in range(N):
    map_.append(list(input()))

    for j in range(M):
        if map_[i][j] == "L": all_land_idx.append((i, j))

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

def solution(start):
    visit = [[0] * M for _ in range(N)]
    visit[start[0]][start[1]] = 1
    queue = deque([(0, *start)])
    count = 0

    while queue:
        c, current_i, current_j = queue.popleft()
        count = c
        for k in range(4):
            next_i, next_j = current_i+di[k], current_j+dj[k]
            if 0 <= next_i < N and 0 <= next_j < M and map_[next_i][next_j] == 'L' and visit[next_i][next_j] == 0:
                    visit[next_i][next_j] = 1
                    queue.append((c+1, next_i, next_j))

    return count

result = 0

for start in all_land_idx:
    result = max(result, solution(start))

print(result)