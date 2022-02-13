import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M = map(int, input().split())

root = [i for i in range(N+2)]

warp = [tuple(map(int, input().split())) for _ in range(M)]
emergency_exit = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    warp.append((0, i, emergency_exit[i]))

warp.sort(key=lambda x: x[2])

def find_root(x):
    if root[x] != x: root[x] = find_root(root[x])
    return root[x]

result = 0

for a, b, c in warp:
    a_root = find_root(a)
    b_root = find_root(b)

    if a_root != b_root:
        result += c

        if emergency_exit[a_root] < emergency_exit[b_root]: root[b_root] = a_root
        else: root[a_root] = b_root

print(result)
