import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

from collections import defaultdict

V, E = map(int, input().split())

data = defaultdict(list)
discovered = [0 for _ in range(V+1)]
result = [False for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())

    data[a].append(b)
    data[b].append(a)

cnt = 0

def dfs(current: int, root: bool):
    global cnt

    cnt += 1
    discovered[current] = cnt # 탐색 순서

    num = discovered[current] # current에서 갈 수 있는 최소 탐색 순서

    child = 0 # 자식 노드의 수.

    for next in data[current]: # current에서 갈 수 있는 노드 반복.

        if discovered[next] == 0: # next를 아직 탐색하지 않았다면

            child += 1 # 자식 노드 + 1
            low = dfs(next, False) # 자식 노드에서 갈 수 있는 최소 탐색 순서
            num = min(num, low) # 자식 노드에서 갈 수 있는 최소 탐색 순서가 current보다 작다면 갱신.

            if not root and low >= discovered[current]: # 자식 노드에서 갈 수 있는 최소 탐색 순서가 current노드의 탐색 순서보다 늦다면 current는 단절점.
                result[current] = True 

        else:
            num = min(num, discovered[next])  # 자식 노드에서 갈 수 있는 최소 탐색 순서가 current보다 작다면 갱신.

    if root and child >= 2: # current가 루트노드이면서 자식노드의 수가 2개 이상이라면
        result[current] = True # current는 단절점.

    return num # current에서 갈 수 있는 최소 탐색 순서를 반환한다.

for i in range(1, V+1):
    if discovered[i] == 0:
        dfs(i, True)

print(result.count(True))
for i in range(1, V+1):
    if result[i]: print(i, end=" ")
