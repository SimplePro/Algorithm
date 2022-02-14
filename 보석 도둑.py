import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
jewel_list = [list(map(int, input().split())) for _ in range(N)]
bag_list = [int(input()) for _ in range(K)]

jewel_list.sort() # 무게가 가벼운 순으로 오름차순 정렬
bag_list.sort() # 담을 수 있는 무게가 가벼운 순으로 오름차순 정렬

result = 0
tmp = [] # 현재 가방이 담을 수 있는 보석가치 리스트

for bag in bag_list: # 모든 가방을 반복
    while jewel_list and bag >= jewel_list[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jewel_list)[1])

    if tmp: result += -heapq.heappop(tmp) # 현재 가방이 담을 수 있는 보석들 중에 가치가 가장 큰 것을 추가함.
    elif not jewel_list: break # 담을 수 있는 남은 보석이 없다면 break.

print(result)