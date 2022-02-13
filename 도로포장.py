from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

road_data = defaultdict(list)

for _ in range(M):
    a, b, t = map(int, input().split())
    road_data[a].append((t, b))
    road_data[b].append((t, a))

time = [[sys.maxsize] * (K+1) for _ in range(N+1)]
for i in range(1, K+1):
    time[1][i] = 0

heap = []
heapq.heappush(heap, (0, 1, 0))

while heap:
    t, current_city, current_k = heapq.heappop(heap)

    if time[current_city][current_k] < t: continue

    if (current_k+1) <= K:
        for next_time, next_city in road_data[current_city]:
            if time[next_city][current_k+1] > t:
                time[next_city][current_k+1] = t
                heapq.heappush(heap, (t, next_city, current_k+1))

    for next_time, next_city in road_data[current_city]:
            if time[next_city][current_k] > t + next_time:
                time[next_city][current_k] = t + next_time
                heapq.heappush(heap, (time[next_city][current_k], next_city, current_k))

print(min(time[-1]))