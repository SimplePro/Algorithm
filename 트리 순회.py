import sys
input = sys.stdin.readline

N = int(input())

graph_data = [(27, 27) for _ in range(N)]

for _ in range(N):
    node, left_child_node, right_child_node = input().split()

    node = ord(node) - ord("A")
    left_child_node = ord(left_child_node) - ord("A") if left_child_node != "." else 27
    right_child_node = ord(right_child_node) - ord("A") if right_child_node != "." else 27

    graph_data[node] = (left_child_node, right_child_node)

visited = [0 for _ in range(N)]
result = []

def preorder(node):
    visited[node] = 1
    result.append(chr(node + ord("A")))

    if graph_data[node][0] != 27 and visited[graph_data[node][0]] == 0:
        preorder(graph_data[node][0])

    if graph_data[node][1] != 27 and visited[graph_data[node][1]] == 0:
        preorder(graph_data[node][1])

preorder(0)

print("".join(result))

visited = [0 for _ in range(N)]
result = []

def inorder(node):
    visited[node] = 1

    if graph_data[node][0] != 27 and visited[graph_data[node][0]] == 0:
        inorder(graph_data[node][0])

    result.append(chr(node + ord("A")))

    if graph_data[node][1] != 27 and visited[graph_data[node][1]] == 0:
        inorder(graph_data[node][1])

inorder(0)

print("".join(result))

visited = [0 for _ in range(N)]
result = []

def postorder(node):
    visited[node] = 1

    if graph_data[node][0] != 27 and visited[graph_data[node][0]] == 0:
        postorder(graph_data[node][0])

    if graph_data[node][1] != 27 and visited[graph_data[node][1]] == 0:
        postorder(graph_data[node][1])

    result.append(chr(node + ord("A")))

postorder(0)

print("".join(result))