import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

M, N = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dp[-1][-1] = 0

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(i, j):

    if i == (M-1) and j == (N-1): return 1
    if dp[i][j] != -1: return dp[i][j]
    
    dp[i][j] = 0

    for k in range(4):
        next_i, next_j = i+di[k], j+dj[k]

        if 0 <= next_i < M and 0 <= next_j < N and data[next_i][next_j] < data[i][j]:
            dp[i][j] += dfs(next_i, next_j)

    return dp[i][j]

print(dfs(0, 0))