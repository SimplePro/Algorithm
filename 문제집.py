import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

heap = []

visit = [0 for _ in range(N+1)]

book_information = [[] for _ in range(N+1)] # book_information[a] = 책 a를 읽은 후 읽어야 하는 책들.
degree = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    book_information[a].append(b)
    degree[b] += 1

for i in range(1, N+1):
    if not degree[i]: heapq.heappush(heap, i)

result = []

while heap:
    book = heapq.heappop(heap)
    result.append(book)

    for next_node in book_information[book]:
        degree[next_node] -= 1
        if not degree[next_node]: heapq.heappush(heap, next_node)

print(" ".join(map(str, result)))