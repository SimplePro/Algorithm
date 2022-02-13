import math
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

tree = [0] * 2**(math.ceil(math.log2(N))+1)
lazy = [0] * 2**(math.ceil(math.log2(N))+1)
data = [0] + [int(input()) for _ in range(N)]

def init(node, left, right):
    if left == right:
        tree[node] = data[left]
        return tree[node]
    else:
        mid = (left+right) // 2

        tree[node] = init(node*2, left, mid) + init(node*2+1, mid+1, right)
        return tree[node]

def update_lazy(node, left, right): # lazy 값을 업데이틀함.
    tree[node] += (right-left+1) * lazy[node] # 현재 node에 반영.
    if left != right: # 자식노드가 있으면
        lazy[node*2] += lazy[node] # 왼쪽 자식
        lazy[node*2+1] += lazy[node] # 오른쪽 자식에게 lazy를 전파
    lazy[node] = 0 # 현재 node의 lazy를 초기화함.

def update(node, left, right, start, end, value): # left, right는 현재 노드가 담당하고 있는 범위. start, end는 변경해야 하는 인덱스 범위.
    update_lazy(node, left, right)

    if right < start or end < left: # 겹치는 범위가 하나도 없으면.
        return
    
    if start <= left and right <= end: # 완전히 포개어지면
        tree[node] += (right-left+1) * value # 현재 node에 반영.
        if left != right: # 자식노드가 있다면ㅑ
            lazy[node*2] += value # 왼쪽 자식
            lazy[node*2+1] += value # 오른쪽 자식에게 lazy를 전파.

    else: # 아니면
        mid = (left+right) // 2
        update(node*2, left, mid, start, end, value)
        update(node*2+1, mid+1, right, start, end, value)
        tree[node] = tree[node*2] + tree[node*2+1]

def sub_sum(node, left, right, start, end): # left, right는 현재 노드가 담당하고 있는 범위. start, end는 구간합을 구해야하는 인덱스 범위.
    update_lazy(node, left, right)

    global result
    if right < start or end < left: return
    elif start <= left and right <= end: result += tree[node]

    else:
        mid = (left+right) // 2
        sub_sum(node*2, left, mid, start, end)
        sub_sum(node*2+1, mid+1, right, start, end)

init(1, 1, N)

for _ in range(M+K):
    command = list(map(int, input().split()))

    if command[0] == 1:
        update(1, 1, N, command[1], command[2], command[3])

    else:
        result = 0
        sub_sum(1, 1, N, command[1], command[2])
        print(result)
