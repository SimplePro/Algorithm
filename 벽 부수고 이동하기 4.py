from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

map_ = []

for _ in range(N):
    map_.append([])
    for i in input()[:-1]:
        map_[-1].append(int(i))

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

grouped_data = defaultdict(int) # grouped_data[(i, j)] = i, j 위치의 그룹번호
group_count = []

def grouping(start, group_number):
    queue = deque([start])
    grouped_data[start] = group_number

    while queue:
        current_i, current_j = queue.popleft()

        for k in range(4):
            next_i = current_i+di[k]
            next_j = current_j+dj[k]

            if 0 <= next_i < N and 0 <= next_j < M and map_[next_i][next_j] == 0 and grouped_data[(next_i, next_j)] == 0:
                group_count[-1] += 1
                grouped_data[(next_i, next_j)] = group_number
                queue.append((next_i, next_j))

group_number = 1

for i in range(N):
    for j in range(M):
        if map_[i][j] == 0 and grouped_data[(i, j)] == 0:
            group_count.append(1)
            grouping((i, j), group_number)
            group_number += 1

def solution(pos):
    result = 1

    group_ = []

    for k in range(4):
        next_i = pos[0]+di[k]
        next_j = pos[1]+dj[k]

        if 0 <= next_i < N and 0 <= next_j < M and map_[next_i][next_j] == 0 and grouped_data[(next_i, next_j)] not in group_:
            result += group_count[grouped_data[(next_i, next_j)]-1]
            group_.append(grouped_data[(next_i, next_j)])

    return result

for i in range(N):
    for j in range(M):
        if map_[i][j] == 1: print(solution((i, j))%10, end="")
        else: print("0", end="")
    print()
