from itertools import combinations

N, M = map(int, input().split())

lab_map = []

for i in range(N):
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


def simulate(virus_ij, map_, empty_count):

    for i, j in virus_ij:
        map_[i][j] = 0

    virus = [*virus_ij]

    while virus:
        i, j = virus.pop(0)

        possible_ij = possible_ij_(i, j, map_)

        for next_i, next_j in possible_ij:
            map_[next_i][next_j] = 1
            empty_count -= 1

            virus.append((next_i, next_j))
    
    return empty_count

all_virus_index = []
all_block_index = []
current_block_index = []
for i in range(N):
    for j in range(M):
        if lab_map[i][j] == 2:
            all_virus_index.append((i, j))

        elif lab_map[i][j] == 0:
            all_block_index.append((i, j))

        else:
            current_block_index.append((i, j))


def make_map(block_ij):
    map_ = [[-1] * M for _ in range(N)]

    for i, j in block_ij + current_block_index:
        map_[i][j] = -2

    return map_

empty_count = len(all_block_index) - 3

result = 0

for comb in list(map(list, combinations(all_block_index, 3))):
    result = max(result, simulate(all_virus_index, make_map(comb), empty_count))

print(result)