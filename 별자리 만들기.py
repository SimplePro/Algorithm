import heapq
import math
import sys
INF = sys.maxsize
input = sys.stdin.readline

N = int(input())

star_data = [tuple(map(float, input().split())) for i in range(N)]

distance_data = [[INF] * N for _ in range(N)]

def distance(a, b):
    return round(math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2), 2)

result = 0

heap = []

for i in range(N):
    for j in range(N):
        d = distance(star_data[i], star_data[j])
        heapq.heappush(heap, (d, (i, j)))

root = [i for i in range(N)]

def find_root(x):
    if root[x] != x: root[x] = find_root(root[x])
    return root[x]

while heap:
    d, stars = heapq.heappop(heap)

    a_root = find_root(stars[0])
    b_root = find_root(stars[1])

    if a_root != b_root:
        result += d
        if a_root <= b_root:
            root[b_root] = a_root

        else:
            root[a_root] = b_root

print(result)