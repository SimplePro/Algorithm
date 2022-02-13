T = int(input())

def solution(N):
    dp = [[0] * 2 + list(map(int, input().split())) for _ in range(2)]

    for i in range(2, N+2):
        dp[0][i] += max(dp[1][i-2:i])
        dp[1][i] += max(dp[0][i-2:i])

    return max(dp[0][-1], dp[1][-1])

for _ in range(T):
    print(solution(int(input())))
