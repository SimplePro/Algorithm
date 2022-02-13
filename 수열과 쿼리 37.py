import math
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
data = [0] + list(map(int, input().split()))

tree = [0] * 2**(math.ceil(math.log2(N))+1) # 홀수 개수

def init(node, left, right):
    if left == right:
        tree[node] = (data[left] % 2)
        return tree[node]

    else:
        mid = (left+right) // 2
        tree[node] = init(node*2, left, mid) + init(node*2+1, mid+1, right)
        return tree[node]
        
def update(node, left, right, idx, value):
    if left == right == idx:
        tree[node] = (value % 2)

    elif idx < left or right < idx: return

    else:
        mid = (left+right) // 2
        update(node*2, left, mid, idx, value)
        update(node*2+1, mid+1, right, idx, value)
        tree[node] = tree[node*2] + tree[node*2+1]

def sub_odd(node, left, right, start, end):
    global result

    if right < start or end < left:
        return
    
    elif start <= left and right <= end:
        result += tree[node]

    else:
        mid = (left+right) // 2
        sub_odd(node*2, left, mid, start, end)
        sub_odd(node*2+1, mid+1, right, start, end)

init(1, 1, N)

M = int(input())

for _ in range(M):
    command = list(map(int, input().split()))

    if command[0] == 1: update(1, 1, N, command[1], command[2])
    else:
        result = 0
        sub_odd(1, 1, N, command[1], command[2])
        
        if command[0] == 2:
            print(command[2] - command[1] + 1 - result)
        
        else:
            print(result)
