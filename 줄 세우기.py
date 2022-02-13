import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)] # graph[a] = a 뒤에 서야하는 학생들.
in_degree = [0 for _ in range(N+1)] # in_degree[a] = a 앞에 서야하는 학생의 수.

result = []

heap = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

for i in range(1, N+1):
    if not in_degree[i]: heapq.heappush(heap, i)

while heap:
    student = heapq.heappop(heap)
    result.append(student)

    for next_student in graph[student]:
        in_degree[next_student] -= 1
        if not in_degree[next_student]: heapq.heappush(heap, next_student)

print(" ".join(map(str, result)))