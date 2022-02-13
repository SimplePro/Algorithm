import sys
input = sys.stdin.readline

N = int(input())
sticks = [int(input()) for _ in range(N)]

MAX = sticks[-1]

count = 1

for i in range(len(sticks)-2, -1, -1):
    if sticks[i] > MAX:
        MAX = sticks[i]
        count += 1

print(count)
