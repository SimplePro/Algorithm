import math
import sys
INF = sys.maxsize
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())

data = [0] + [int(input()) for _ in range(N)]
min_tree = [0] * 2**(math.ceil(math.log2(N))+1)
max_tree = [0] * 2**(math.ceil(math.log2(N))+1)

def min_init(node, left, right):
    if left == right:
        min_tree[node] = data[left]
        return min_tree[node]

    else:
        mid = (left+right) // 2
        min_tree[node] = min(min_init(node*2, left, mid), min_init(node*2+1, mid+1, right))
        return min_tree[node]

def max_init(node, left, right):
    if left == right:
        max_tree[node] = data[left]
        return max_tree[node]

    else:
        mid = (left+right) // 2
        max_tree[node] = max(max_init(node*2, left, mid), max_init(node*2+1, mid+1, right))
        return max_tree[node]

def sub_min(node, left, right, start, end):
    global min_result

    if right < start or end < left:
        return

    elif start <= left and right <= end:
        min_result = min(min_result, min_tree[node])

    else:
        mid = (left+right) // 2
        sub_min(node*2, left, mid, start, end)
        sub_min(node*2+1, mid+1, right, start, end)


def sub_max(node, left, right, start, end):
    global max_result

    if right < start or end < left:
        return

    elif start <= left and right <= end:
        max_result = max(max_result, max_tree[node])

    else:
        mid = (left+right) // 2
        sub_max(node*2, left, mid, start, end)
        sub_max(node*2+1, mid+1, right, start, end)

min_init(1, 1, N)
max_init(1, 1, N)

for _ in range(M):
    l, r = map(int, input().split())

    min_result, max_result = INF, -INF
    sub_min(1, 1, N, l, r)
    sub_max(1, 1, N, l, r)

    print(min_result, max_result)
