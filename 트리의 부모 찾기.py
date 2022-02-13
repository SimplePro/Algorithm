import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

from collections import defaultdict

N = int(input())

graph_data = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph_data[a].append(b)
    graph_data[b].append(a)

is_visited = [0 for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

def dfs(node):
    is_visited[node] = 1

    for next_node in graph_data[node]:
        if is_visited[next_node] == 0:
            parent[next_node] = node
            dfs(next_node)

dfs(1)

for i in range(2, N+1):
    print(parent[i])