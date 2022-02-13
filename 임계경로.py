from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

city_data = defaultdict(list) # city_data[i] = 도시 i에서 갈 수 있는 도시들.
in_degree = [0 for _ in range(N+1)] # in_degree[i] = 도시 i로 올 수 있는 도시의 개수.

for _ in range(M):
    start_city, end_city, time = map(int, input().split())
    city_data[start_city].append((time, end_city))
    in_degree[end_city] += 1

queue = deque([])

from_city, to_city = map(int, input().split())

queue.append(from_city)

time_path_data = [[0, []] for _ in range(N+1)] # time_path_data[i] = 출발도시에서 도시i로 갈때까지 가장 오래 걸리는 시간과 경로.
time_path_data[from_city] = [0, [from_city]]

while queue:
    current_city = queue.popleft()

    for next_time, next_city in city_data[current_city]:
        in_degree[next_city] -= 1

        update_time = time_path_data[current_city][0] + next_time

        if time_path_data[next_city][0] < update_time:
            time_path_data[next_city][0] = update_time
            time_path_data[next_city][1] = time_path_data[current_city][1] + [next_city]
        
        elif time_path_data[next_city][0] == update_time:
            time_path_data[next_city][1] = time_path_data[current_city][1] + [next_city]
        
        if in_degree[next_city] == 0:
            queue.append(next_city)

for result in time_path_data[to_city]:
    print(result)
