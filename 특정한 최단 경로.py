from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph_data = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph_data[a].append((c, b))
    graph_data[b].append((c, a))

a, b = map(int, input().split())

def dijkstra(start, end):
    distance = [sys.maxsize for _ in range(N+1)]
    distance[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        d, current_node = heapq.heappop(heap)

        if distance[current_node] < d: continue

        for next_dis, next_node in graph_data[current_node]:
            update_dis = next_dis + d

            if update_dis < distance[next_node]:
                distance[next_node] = update_dis
                heapq.heappush(heap, (distance[next_node], next_node))

    return distance[end]

a_to_b = dijkstra(a, b) # = b_to_a

start_to_a = dijkstra(1, a)
b_to_end = dijkstra(b, N)

start_to_b = dijkstra(1, b)
a_to_end = dijkstra(a, N)

type1_ = start_to_a != sys.maxsize and a_to_b != sys.maxsize and b_to_end != sys.maxsize
type2_ = start_to_b != sys.maxsize and a_to_b != sys.maxsize and a_to_end != sys.maxsize

if not type1_ and not type2_:
    print(-1)
    sys.exit()
else:
    print(min(start_to_a + a_to_b + b_to_end, start_to_b + a_to_b + a_to_end))
