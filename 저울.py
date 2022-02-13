from collections import defaultdict

N = int(input())
M = int(input())

heavy_data = defaultdict(list) # greater_data[i] = 물건 i보다 무거운 물건들.
light_data = defaultdict(list) # smaller_data[i] = 물건 i보다 가벼운 물건들.

for _ in range(M):
    a, b = map(int, input().split()) # a > b
    heavy_data[b].append(a)
    light_data[a].append(b)

result = N

def solution(start_stuff):
    global result
    result = N
    visited = [0 for _ in range(N+1)]

    def heavy_dfs(stuff):
        global result

        if not visited[stuff]:
            visited[stuff] = 1
            result -= 1

            for next_stuff in heavy_data[stuff]:
                heavy_dfs(next_stuff)

    def light_dfs(stuff):
        global result

        if not visited[stuff]:
            visited[stuff] = 1
            result -= 1

            for next_stuff in light_dfs[stuff]:
                light_dfs(next_stuff)

    heavy_dfs(start_stuff)
    light_dfs(start_stuff)

    return result

for i in range(1, N+1):
    print(solution(i))