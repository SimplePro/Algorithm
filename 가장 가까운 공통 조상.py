import sys
sys.setrecursionlimit(100000)

def solution():
    N = int(input())
    tree_data = {}

    for _ in range(N-1):
        root, node = map(int, input().split())
        tree_data[node] = root

    def dfs1(path):
        if path[-1] in tree_data.keys():
            return dfs1(path + [tree_data[path[-1]]])

        else:
            return path

    a, b = map(int, input().split())

    a_path = dfs1([a])

    def dfs2(current_node):
        if current_node in a_path:
            return current_node
        
        else:
            return dfs2(tree_data[current_node])

    result = dfs2(b)
    
    return result

result_list = []

T = int(input())

for _ in range(T):
    result_list.append(solution())

for i in range(T):
    print(result_list[i])