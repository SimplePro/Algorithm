X = " " + input()
Y = " " + input()
Z = " " + input()

dp = [[[0] * len(Z) for _ in range(len(Y))] for _ in range(len(X))]

di, dj, dk = [-1, 0, 0, -1, -1, 0], [0, -1, 0, -1, 0, -1], [0, 0, -1, 0, -1, -1]

result = 0

for i in range(1, len(X)):
    for j in range(1, len(Y)):
        for k in range(1, len(Z)):
            if X[i] == Y[j] == Z[k]: dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                max_ = 0
                for plus_idx in range(6):
                    before_i, before_j, before_k = i+di[plus_idx], j+dj[plus_idx], k+dk[plus_idx]
                    max_ = max(max_, dp[before_i][before_j][before_k])
                
                dp[i][j][k] = max_

            result = max(result, dp[i][j][k])

print(result)
