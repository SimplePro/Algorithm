import sys
input = sys.stdin.readline

from collections import defaultdict, deque

N = int(input())
M = int(input())

graph_data = [[] * (N+1) for _ in range(N+1)] # graph_data[i] = 지점 i에서 바로 갈 수 있는 지점들과 그 거리
in_degree = [0 for _ in range(N+1)] # in_degree[i] = 지점 i의 선행지점의 개수.

for _ in range(M):
    a, b, w = map(int, input().split())
    graph_data[a].append((w, b))
    in_degree[b] += 1

queue = deque([1])

dp = [[0, []] for _ in range(N+1)] # dp[i] = 1에서 지점i로 가는 최대 점수와 그 경로.
dp[1] = [0, [1]]

while queue:
    current_node = queue.popleft()

    for next_score, next_node in graph_data[current_node]:
        in_degree[next_node] -= 1

        if dp[current_node][0] + next_score > dp[next_node][0]:
            dp[next_node][0] = dp[current_node][0] + next_score
            dp[next_node][1] = dp[current_node][1] + [next_node]

        if in_degree[next_node] == 0 and next_node != 1:
            queue.append(next_node)

print(dp[1][0])
print(" ".join(map(str, dp[1][1])))
