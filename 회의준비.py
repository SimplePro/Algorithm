import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

from collections import defaultdict

N = int(input())
M = int(input())

distance_data = [[101] * (N+1) for _ in range(N+1)] # distance_data[i][j] = i에서 j로 갈때 거쳐야 하는 최소 간선의 개수.
is_visited = [0 for _ in range(N+1)]
graph_data = defaultdict(list) # graph_data[i] = 노드 i에서 갈 수 있는 노드들.

for _ in range(M):
    a, b = map(int, input().split())

    graph_data[a].append(b)
    graph_data[b].append(a)

    distance_data[a][b] = 1
    distance_data[b][a] = 1

grouped_data = []

def grouping_dfs(current):
    is_visited[current] = 1
    grouped_data[-1].append(current)

    for next_node in graph_data[current]:
        if is_visited[next_node] == 0: grouping_dfs(next_node)

for i in range(1, N+1):
    if is_visited[i] == 0:
        grouped_data.append([])
        grouping_dfs(i)

def solution(members, size):
    result = []

    for m1 in members:
        result.append([])
        for m2 in members:
            if m1 == m2: result[-1].append(0)
            else: result[-1].append(distance_data[m1][m2])

    for i in range(size):
        result[i][i] = 0

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if result[i][k] + result[k][j] < result[i][j]:
                    result[i][j] = result[i][k] + result[k][j]

    for i in range(size):
        result[i] = max(result[i])

    return members[result.index(min(result))]

ans = []

for members in grouped_data:
    ans.append(solution(members, len(members)))

ans.sort()

print(len(ans))

for i in range(len(ans)):
    print(ans[i])