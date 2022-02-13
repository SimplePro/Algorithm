import heapq
import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
item_list = set()
item_data = defaultdict(list) # item_data[A] = 아이템 A를 선행 아이템으로 쓰는 아이템들
in_degree = defaultdict(int) # in_degree[A] = A의 선행작업의 개수.

for _ in range(N):
    A, B = input().split()
    item_data[A].append(B)
    in_degree[B] += 1

    item_list.add(A)
    item_list.add(B)

heap = []
update_heap = []

item_list = list(item_list)

for item in item_list:
    if in_degree[item] == 0: heapq.heappush(heap, item)

result = []

while heap:
    current_item = heapq.heappop(heap)
    result.append(current_item)

    for next_item in item_data[current_item]:
        in_degree[next_item] -= 1

        if in_degree[next_item] == 0:
            heapq.heappush(update_heap, next_item)

    if not heap:
        heap = update_heap[:]
        heapq.heapify(heap)
        update_heap = []

if len(result) == len(item_list):
    for item in result:
        print(item)

else:
    print(-1)
