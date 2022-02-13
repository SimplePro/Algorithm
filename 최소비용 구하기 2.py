from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = defaultdict(list) # graph[i] = 도시 i에서 갈 수 있는 도시들과 거리.

for _ in range(M):
    start_city, end_city, dis = map(int, input().split())
    graph[start_city].append((dis, end_city))

start_city, end_city = map(int, input().split())
path = [[] for i in range(N+1)] # path[i] = 시작 도시에서 도시 i까지 가는 최단경로
path[start_city].append(start_city)

distance = [float('inf') for _ in range(N+1)]
distance[start_city] = 0

heap = []
heapq.heappush(heap, (0, start_city))

while heap:
    dis, city = heapq.heappop(heap)

    if distance[city] < dis: continue

    for next_dis, next_city in graph[city]:
        next_distance = next_dis + dis

        if next_distance < distance[next_city]:
            distance[next_city] = next_distance
            path[next_city] = path[city] + [next_city]

            heapq.heappush(heap, (next_distance, next_city))

print(distance[end_city])
print(len(path[end_city]))
print(*path[end_city])