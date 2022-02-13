import sys
input = sys.stdin.readline

N, S = map(int, input().split())

data = list(map(int, input().split()))

sum_ = 0
result = sys.maxsize

start, end = 0, 0

while True:
    if sum_ >= S:
        result = min(result, end - start)
        sum_ -= data[start]
        start += 1

    elif end == N: break

    else:
        sum_ += data[end]
        end += 1

if result == sys.maxsize: print(0)
else: print(result)