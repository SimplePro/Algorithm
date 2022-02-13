# 각 건물당 지어진 개수를 count한다.
# 만약 count가 0인데, 건물이 파괴되었다면 치트키를 사용한 것이다.
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
building_count = [0 for _ in range(N+1)]

graph = [[] for _ in range(N+1)] # graph[A] = 건물 A

for _ in range(M):
    X, Y = map(int, input().split()) # X는 Y의 선행작업.
    graph[Y].append(X)

for _ in range(K):
    command, a = map(int, input().split())

    if command == 1:
        for i in graph[a]:
            if building_count[i] == 0:
                print("Lier!")
                sys.exit()

        building_count[a] += 1
    
    elif command == 2:
        if building_count[a] == 0:
            print("Lier!")
            sys.exit()
        building_count[a] -= 1
    
print("King-God-Emperor")