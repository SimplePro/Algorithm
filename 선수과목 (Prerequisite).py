from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

in_degree = [0 for _ in range(N+1)]
preceding_data = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    preceding_data[a].append(b)
    in_degree[b] += 1

count = 1

result = [0 for _ in range(N+1)]

queue = deque([])

for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)

update_queue = deque([])

while queue:
    current_subject = queue.popleft()
    result[current_subject] = count

    for next_subject in preceding_data[current_subject]:
        in_degree[next_subject] -= 1

        if in_degree[next_subject] == 0:
            update_queue.append(next_subject)

    if not queue:
        queue = update_queue
        update_queue = deque([])
        count += 1

print(" ".join(map(str, result[1:])))