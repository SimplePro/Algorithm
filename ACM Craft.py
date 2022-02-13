from collections import defaultdict, deque
import sys
input = sys.stdin.readline

T = int(input())

def solution():
    N, K = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))

    building_data = defaultdict(list) # building_data[i] = 건물 i를 선수건물로 사용하고 있는 건물들.
    in_degree = [0 for _ in range(N+1)] # in_degree[i] = 건물 i를 짓기 전에 지어야 하는 건물의 개수

    dp = [0] * (N+1) # dp[i] = 건물 i를 짓기까지 소요된 시간 = 건물 i의 선수건물들의 최대 건설시간 + 건물 i의 건설시간

    

    for _ in range(K):
        X, Y = map(int, input().split())
        building_data[X].append(Y)
        in_degree[Y] += 1
    
    W = int(input())

    queue = deque([])

    for i in range(1, N+1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = build_time[i]

    while queue:
        current_building = queue.popleft()

        for next_building in building_data[current_building]:
            in_degree[next_building] -= 1

            dp[next_building] = max(dp[next_building], dp[current_building] + build_time[next_building])

            if in_degree[next_building] == 0:
                queue.append(next_building)

    return dp[W]

for _ in range(T):
    print(solution())
