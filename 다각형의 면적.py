import sys
input = sys.stdin.readline

N = int(input())

data = [tuple(map(int, input().split())) for _ in range(N)]
data += [data[0]]

a, b = 0, 0

for i in range(N):
    a += data[i][0] * data[i+1][1]

for i in range(1, N+1):
    b += data[i][0] * data[i-1][1]

print(round(abs(a-b)/2, 1))
