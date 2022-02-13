import math
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, Q = map(int, input().split())
data = [0] + list(map(int, input().split()))

tree = [0] * 2**(math.ceil(math.log2(N))+1)

def init(node, left, right):
    if left == right:
        tree[node] = data[left]
        return tree[node]

    else:
        mid = (left+right) // 2
        tree[node] = init(node*2, left, mid) + init(node*2+1, mid+1, right)
        return tree[node]

init(1, 1, N)

def update(node, left, right, idx, value):
    if left == right == idx:
        tree[node] = value
        return

    elif idx < left or right < idx:
        return
    
    else:
        mid = (left+right) // 2
        update(node*2, left, mid, idx, value)
        update(node*2+1, mid+1, right, idx, value)
        tree[node] = tree[node*2] + tree[node*2+1]
        return


def sub_sum(node, left, right, start, end):
    global result
    if start <= left and right <= end:
        result += tree[node]
        return
    
    elif right < start or end < left:
        return

    else:
        mid = (left+right) // 2
        sub_sum(node*2, left, mid, start, end)
        sub_sum(node*2+1, mid+1, right, start, end)

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x > y: x, y = y, x
    result = 0
    sub_sum(1, 1, N, x, y)
    print(result)
    update(1, 1, N, a, b)
