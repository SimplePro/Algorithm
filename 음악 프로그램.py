from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list) # graph[n] = n의 앞에 서야 하는 사람들.
in_degree = [0 for _ in range(N+1)] # in_degree[n] = n의 뒤에 서야 하는 사람들의 수.
queue = deque([])

for _ in range(M):
    data = list(map(int, input().split()))

    for i in range(data[0]-1):
        graph[data[i+2]].append(data[i+1])
        in_degree[data[i+1]] += 1

for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)

result = []

while queue:
    singer = queue.popleft()
    result.append(singer)

    for next_singer in graph[singer]:
        in_degree[next_singer] -= 1

        if in_degree[next_singer] == 0:
            queue.append(next_singer)

if len(result) != N: print(0)
else:
    for singer in result[::-1]:
        print(singer)