import math
import sys
INF = sys.maxsize
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M, K = map(int, input().split())
tree = [INF] * 2**math.ceil(math.log2(N)+1)

data = [int(input()) for _ in range(N)]

def init(node, start, end):
    if start == end:
        tree[node] = data[start]
        return tree[node]

    else:
        mid = (start+end) // 2

        tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
        return tree[node]

init(1, 0, N-1)

def update(node, start, end, idx, update_data):
    if start == end == idx:
        tree[node] = update_data
        return tree[node]
    if idx < start or end < idx: return

    else:
        mid = (start+end) // 2
        update(node*2, start, mid, idx, update_data)
        update(node*2+1, mid+1, end, idx, update_data)
        tree[node] = tree[node*2] + tree[node*2+1]

def sub_sum(node, start, end, left, right):
    global result

    if end < left or right < start: return
    elif left <= start and end <= right:
        result += tree[node]
        return

    else:
        mid = (start+end) // 2
        sub_sum(node*2, start, mid, left, right)
        sub_sum(node*2+1, mid+1, end, left, right)

for _ in range(M+K):
    result = 0

    a, b, c = map(int, input().split())

    if a == 1:
        update(1, 0, N-1, b-1, c)

    elif a == 2:
        sub_sum(1, 0, N-1, b-1, c-1)
        print(result)