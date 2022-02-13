import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split()) 
root = [i for i in range(N+1)]

def find_root(x):
    if root[x] != x: root[x] = find_root(root[x])
    return root[x]

for _ in range(M):
    command, a, b = map(int, input().split())

    a_root = find_root(a)
    b_root = find_root(b)

    if command == 0:
        if a_root != b_root:
            if a_root < b_root:
                root[b_root] = a_root
            else:
                root[a_root] = b_root

    elif command == 1:
        print("YES" if a_root == b_root else "NO")