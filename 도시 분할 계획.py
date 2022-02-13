import sys
input = sys.stdin.readline

N, M = map(int, input().split())

road_data = [list(map(int, input().split())) for _ in range(M)]
road_data.sort(key=lambda x: x[2])

root = [i for i in range(N+1)]

def find_root(x):
    if root[x] != x:
        root[x] = find_root(root[x])
    return root[x]

cost = 0
count = 0

for a, b, c in road_data:
    a_root = find_root(a)
    b_root = find_root(b)

    if a_root != b_root:
        if a_root < b_root:
            root[b_root] = a_root
        else:
            root[a_root] = b_root

        cost += c
        count += 1
    
    if count == (N-2): break

print(cost)