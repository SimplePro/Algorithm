import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def solution(N):

    map_ = [list(map(int, input().split())) for _ in range(N)]

    cost_list = [[INF] * N for _ in range(N)] # cost_list[i][j] = 0, 0에서 i, j로 가는데까지 잃은 루피의 최소값.
    cost_list[0][0] = map_[0][0]

    heap = []
    heapq.heappush(heap, (cost_list[0][0], (0, 0)))

    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

    while heap:
        c, ij = heapq.heappop(heap)
        i, j = ij

        if cost_list[i][j] < c: continue

        for k in range(4):
            next_i, next_j = i+di[k], j+dj[k]
            if 0 <= next_i < N and 0 <= next_j < N:
                next_cost = c + map_[next_i][next_j]

                if cost_list[next_i][next_j] > next_cost:
                    cost_list[next_i][next_j] = next_cost
                    heapq.heappush(heap, (next_cost, (next_i, next_j)))

    return cost_list[-1][-1]

cnt = 1

while True:
    N = int(input())
    if N == 0: break
    print(f"Problem {cnt}: {solution(N)}")
    cnt += 1