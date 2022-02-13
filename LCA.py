# # leaf node에서 가장 위의 루트까지 탐색을 하고, 그 과정에서 탐색했던 루트노드에도 바로 그 위의 루트노드를 추가해주는 형식으로 진행한다.
# # dfs에서도 이미 탐색했던 루트노드이면, 그 루트노드의 탐색결과를 현재 결과에 더해주고 끝.

# N = int(input())
# graph = [0 for _ in range(N+1)] # graph[자식] = 직속조상
# c = [0 for _ in range(N+1)] # c[조상] = 직속자식 수

# for _ in range(N-1):
#     root, leaf = map(int, input().split())
#     graph[leaf] = root
#     c[root] += 1

# M = int(input())
# q = [tuple(map(int, input().split())) for _ in range(M)]

# leaf_nodes = []

# for i in range(2, N+1):
#     if c[i] == 0: leaf_nodes.append(i)
# c = []

# visited = [0 for _ in range(N+1)]
# all_path = [[] for _ in range(N+1)]
# path = []

# print(graph, leaf_nodes)

# def dfs():
#     print(path)
#     if path[-1] == 1:
#         for node in path:
#             visited[node] = 1

#     else:
#         next_root = graph[path[-1]]
#         if visited[next_root]:
#             for node in path:
#                 visited[node] = 1
#                 all_path[node].extend(all_path[next_root])

#         else:
#             path.append(next_root)
#             dfs()
#             path.remove(next_root)


# # for leaf_node in leaf_nodes:
# #     path.append(leaf_node)
# #     dfs()
# #     path.remove(leaf_node)

# print(all_path)
