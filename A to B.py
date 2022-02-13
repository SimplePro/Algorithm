import sys

A, B = map(int, input().split())

result = sys.maxsize

def dfs(d, depth):
    global result
    if d > B: return
    if d == B:
        result = min(result, depth)

    else:
        dfs(d*2, depth+1)
        dfs(int(str(d)+'1'), depth+1)

dfs(A, 1)

if result == sys.maxsize: print(-1)
else: print(result)