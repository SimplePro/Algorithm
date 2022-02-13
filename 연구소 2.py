from itertools import combinations

N, M = map(int, input().split())

lab_map = []

for _ in range(N):
    lab_map.append(list(map(int, input().split())))

def possible_ij_(current_i, current_j, current_map):
    result_ij = []

    if 0 < current_i and current_map[current_i-1][current_j] == -1: # 상
        result_ij.append((current_i-1, current_j))

    if current_i < (N-1) and current_map[current_i+1][current_j] == -1: # 하
        result_ij.append((current_i+1, current_j))

    if 0 < current_j and current_map[current_i][current_j-1] == -1: # 좌
        result_ij.append((current_i, current_j-1))

    if current_j < (N-1) and current_map[current_i][current_j+1] == -1: # 우
        result_ij.append((current_i, current_j+1))

    return result_ij
    

def isitright(current_map):

    for i in range(N):
        for j in range(N):
            if current_map[i][j] == -1:
                return False
    
    return True

def simulate(virus_ij, map_):

    for i, j in virus_ij:
        map_[i][j] = 0

    virus = [*virus_ij]

    result = 0

    while virus:
        i, j = virus.pop(0)

        possible_ij = possible_ij_(i, j, map_)

        for next_i, next_j in possible_ij:
            map_[next_i][next_j] = map_[i][j] + 1

            result = max(result, map_[next_i][next_j])
            virus.append((next_i, next_j))
    
    if isitright(map_): return result
    return 1e21

all_virus_index = []
for i in range(N):
    for j in range(N):
        if lab_map[i][j] == 2:
            all_virus_index.append((i, j))


def make_map():

    map_ = [[-1]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if lab_map[i][j] == 1:
                map_[i][j] = -2

    return map_

min_time = 1e21

for comb in list(combinations(all_virus_index, M)):
    time = simulate(comb, make_map())
    min_time = min(min_time, time)

if min_time == 1e21: print(-1)
else: print(min_time)
