import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

result = []

def dfs(sequence):
    if len(sequence) == M: result.append(sequence)

    else:
        for i in range(sequence[-1], N+1):
            dfs(sequence + [i])

for i in range(1, N+1):
    dfs([i])

for i in range(len(result)):
    result[i] = " ".join(map(str, result[i]))

for res in sorted(set(result)):
    print(res)
