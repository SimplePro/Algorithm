import heapq
import sys
input = sys.stdin.readline

N = int(input())

left_heap = []
right_heap = []

result = []

for i in range(N):
    n = int(input())
    if len(left_heap) != len(right_heap): heapq.heappush(right_heap, (n, n))
    else: heapq.heappush(left_heap, (-n, n))

    if i == 0:
        result.append(left_heap[0][1])
        continue
    elif left_heap[0][1] > right_heap[0][1]:
        left_n = heapq.heappop(left_heap)[1]
        right_n = heapq.heappop(right_heap)[1]

        heapq.heappush(left_heap, (-right_n, right_n))
        heapq.heappush(right_heap, (left_n, left_n))

    result.append(left_heap[0][1])

for i in result:
    print(i)