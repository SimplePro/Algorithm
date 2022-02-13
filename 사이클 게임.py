import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    root = [i for i in range(N)]
    data = [tuple(map(int, input().split())) for _ in range(M)]

    def find_root(x):
        if root[x] != x: root[x] = find_root(root[x])
        return root[x]

    for i in range(M):
        a_root = find_root(data[i][0])
        b_root = find_root(data[i][1])

        if a_root != b_root:
            if a_root <= b_root:
                root[b_root] = a_root
            
            else:
                root[a_root] = b_root

        else:
            return (i+1)

    return 0
        
print(solution())