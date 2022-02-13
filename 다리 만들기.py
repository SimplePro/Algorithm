import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

map_ = [list(map(int, input().split())) for _ in range(N)]

all_land_idx = []

for i in range(N):
    for j in range(N):
        if map_[i][j]: all_land_idx.append((i, j))

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

remain_land = set(all_land_idx[:])
group_data = dict()

def grouping(start):
    queue = deque([start])
    grouped_idx = set()

    while queue:
        i, j = queue.popleft()

        map_[i][j] = group_number
        group_data[(i, j)] = group_number
        grouped_idx.add((i, j))

        for k in range(4):
            next_i, next_j = i+di[k], j+dj[k]
            if 0 <= next_i < N and 0 <= next_j < N and map_[next_i][next_j] == 1:
                queue.append((next_i, next_j))

    queue = []

    return grouped_idx

group_number = 2
while remain_land:
    remain_land -= grouping(remain_land.pop())
    group_number += 1

map_ = []

def step(start):
    queue = deque([(0, *start)])

    while queue:
        count, i, j = queue.popleft()

        for k in range(4):
            next_i, next_j = i+di[k], j+dj[k]

            if 0 <= next_i < N and 0 <= next_j < N:
                if (next_i, next_j) not in group_data:
                    queue.append((count+1, next_i, next_j))

                elif group_data[start] != group_data[(next_i, next_j)]:
                    return count

    return 10000

result = 10000
for start in all_land_idx:
    result = min(result, step(start))

print(result)
