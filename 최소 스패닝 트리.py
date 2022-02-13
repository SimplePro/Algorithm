import sys
input = sys.stdin.readline

V, E = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(E)]
data.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]

def find_parent(x):
    if parent[x] != x: # 자기자신이 부모노드가 아니라면
        parent[x] = find_parent(parent[x]) # 자신의 부모노드를 부모노드의 부모노드로 업데이트.
    return parent[x] # 부모노드 반환.

result = 0

for start, end, weight in data:
    start_parent = find_parent(start)
    end_parent = find_parent(end)

    if start_parent != end_parent:
        result += weight

        if start_parent < end_parent: parent[end_parent] = parent[start_parent]
        else: parent[start_parent] = parent[end_parent]

print(result)