from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())

city_data = defaultdict(list)

for _ in range(M):
    start_city, end_city, t = map(int, input().split())
    city_data[start_city].append((t, end_city))

def solution(start, end):
    time = [10000000 for _ in range(N+1)]
    time[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        t, current_city = heapq.heappop(heap)

        if time[current_city] < t: continue

        for next_time, next_city in city_data[current_city]:
            update_time = next_time + t

            if time[next_city] > update_time:
                time[next_city] = update_time
                heapq.heappush(heap, (time[next_city], next_city))

    return time[end]

result = 0

for s in range(1, N+1):
    start_to_x = solution(s, X)
    x_to_start = solution(X, s)

    result = max(result, start_to_x + x_to_start)

print(result)