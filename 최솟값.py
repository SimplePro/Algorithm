import math
import sys
sys.setrecursionlimit(10**7)
INF = sys.maxsize
input = sys.stdin.readline

N, M = map(int, input().split())

data = [int(input()) for _ in range(N)]

tree = [INF] * 2**math.ceil(math.log2(N)+1)

def next_node_start_end(start, end):
    left_node_start, left_node_end = start, (start+end)//2
    right_node_start, right_node_end = left_node_end + 1, end

    return left_node_start, left_node_end, right_node_start, right_node_end

def init(node, start, end):
    if start == end:
        tree[node] = data[start]
        return tree[node]

    else:
        left_node_start, left_node_end, right_node_start, right_node_end = next_node_start_end(start, end)

        tree[node] = min(init(node*2, left_node_start, left_node_end), init(node*2+1, right_node_start, right_node_end))
        return tree[node]

def sub_min(node, start, end, left, right):
    global result

    if left > end or right < start: return # 두 범위가 겹치지 않으면 탐색 멈춤.
    if left <= start and end <= right: # start, end 범위가 left, right 범위 안에 완전히 포개어져있으면 추가적으로 탐색할 필요가 없다.
        result = min(result, tree[node])
        return
         

    left_node_start, left_node_end, right_node_start, right_node_end = next_node_start_end(start, end)
    sub_min(node*2, left_node_start, left_node_end, left, right)
    sub_min(node*2+1, right_node_start, right_node_end, left, right)

init(1, 0, N-1)

for _ in range(M):
    result = INF
    l, r = map(int, input().split())
    sub_min(1, 0, N-1, l-1, r-1)
    print(result)
