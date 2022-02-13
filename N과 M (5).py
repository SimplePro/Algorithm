import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

visited = [False] * N
result = []

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                result.append(data[i])
                dfs(depth+1)
                result.pop()
                visited[i] = False

dfs(0)