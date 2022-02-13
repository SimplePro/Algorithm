n, m = map(int, input().split())

relate_data = [[] for _ in range(n)]
compliment_data = [0 for _ in range(n)]

data = list(map(int, input().split()))

for i in range(1, n):
    relate_data[data[i]-1].append(i)

for _ in range(m):
    i, w = map(int, input().split())
    compliment_data[i-1] = w

def dfs(node):
    if relate_data[node]: # 부하 직원이 있다면
        for i in relate_data[node]:
            compliment_data[i] += compliment_data[node] # 부하 직원을 자신의 칭찬 가중치만큼 칭찬한다.
            dfs(i)

dfs(0)

print(*compliment_data)
