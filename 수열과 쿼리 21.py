import math
import sys
from unittest import result
input = sys.stdin.readline

N = int(input())
data = [0] + list(map(int, input().split()))

tree = [0] * 2**(math.ceil(math.log2(N))+1)
lazy = [0] * 2**(math.ceil(math.log2(N))+1)

def debug_lazy():
    s = ""

    for i in range(len(lazy)):
        s += f"node {i}: {lazy[i]}, "
    
    s = s[:-2]

    return s

def init(node, start, end):
    if start == end:
        tree[node] = data[start]

    else:
        mid = (start+end) // 2
        init(node*2, start, mid)
        init(node*2+1, mid+1, end)

def update_lazy(node, start, end):
    # print(f"node: {node}, range: {start}-{end},\nlazy | {debug_lazy()}\n")
    if start == end: tree[node] += lazy[node]
    if start != end:
        lazy[node*2] += lazy[node]
        lazy[node*2+1] += lazy[node]
    lazy[node] = 0

def update(node, start, end, left, right, value):
    update_lazy(node, start, end)

    if end < left or right < start: return
    
    elif left <= start and end <= right:
        if start == end: lazy[node] += value
        if start != end:
            lazy[node*2] += value
            lazy[node*2+1] += value

        # print(f"result of lazy was updated: {debug_lazy()}\n")
        
    else:
        mid = (start+end) // 2
        update(node*2, start, mid, left, right, value)
        update(node*2+1, mid+1, end, left, right, value)

def get_query(node, start, end, idx):
    update_lazy(node, start, end)

    if idx < start or end < idx: return
    elif start == end: return tree[node]

    else:
        mid = (start+end) // 2
        left_node = get_query(node*2, start, mid, idx)
        right_node = get_query(node*2+1, mid+1, end, idx)
        if left_node != None: return left_node
        elif right_node != None: return right_node

M = int(input())

init(1, 1, N)

for _ in range(M):
    command = list(map(int, input().split()))

    if command[0] == 1:
        update(1, 1, N, command[1], command[2], command[3])
    
    else:
        print(get_query(1, 1, N, command[1]))