N = int(input())
M = int(input())

computer_data = [list(map(int, input().split())) for _ in range(M)]
computer_data.sort(key=lambda x: x[2])

root_data = [i for i in range(N+1)]

def find_root(x):
    if root_data[x] != x:
        root_data[x] = find_root(root_data[x])
    return root_data[x]

result = 0

for c1, c2, cost in computer_data:
    c1_root = find_root(c1)
    c2_root = find_root(c2)

    if c1_root == c2_root: continue

    if c1_root < c2_root: root_data[c2_root] = c1_root # 자기자신의 루트였던 computer2의 루트의 루트를 computer1의 루트로 바꾼다.
    else: root_data[c1_root] = c2_root # 그 반대의 경우.
    result += cost

print(result)