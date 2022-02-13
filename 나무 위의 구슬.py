# K % 2 == 0이면 오른쪽 노드, K % 2 == 1이면 왼쪽 노드로 감.
# depth가 늘어날수록 K := (K//2) + (K % 2)로 업데이트한다.
# 업데이트하면서 leaf node에 도달하게 되면, 그 leaf node가 바로 K번째 구슬이 떨어지는 노드이다.

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
graph = [0 for _ in range(N+1)] # graph[CURRENT] = CURRENT 노드의 직속자식 노드.

for CURRENT in range(1, N+1):
    LEFT, RIGHT = map(int, input().split())

    graph[CURRENT] = (LEFT, RIGHT)

K = int(input())

def dfs(current):
    global K

    if graph[current] == (-1, -1):
        print(current)
        sys.exit()
    
    if graph[current][0] == -1: # 왼쪽 노드가 없으면
        dfs(graph[current][1]) # 오른쪽 노드로 그대로 감

    elif graph[current][1] == -1: # 오른쪽 노드가 없으면
        dfs(graph[current][0]) # 왼쪽 노드로 그대로 감

    else:
        is_left = K % 2 == 1 # K % 2 == 1이면 왼쪽 노드로 감. 아니면 오른쪽 노드.
        K = (K // 2) + (K % 2) # K update.

        if is_left: # 왼쪽 노드로 가야되면
            dfs(graph[current][0]) # 왼쪽 노드로 감.
        
        else: # 아니면
            dfs(graph[current][1]) # 오른쪽 노드

dfs(1)