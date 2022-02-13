n = int(input())
R = []

for i in range(n):
    R.append(int(input()))

max_v = 10**9 * (-1)
min_v = R[0]

for i in range(1, n):
    max_v = max(max_v, R[i] - min_v)
    min_v = min(min_v, R[i])

print(max_v)