from bisect import bisect_left

m, n = map(int, input().split())

data = []

for i in range(m):
    a = list(map(int, input().split()))
    sorted_a = sorted(a)
    data.append([])

    for j in range(n):

        data[-1].append(bisect_left(sorted_a, a[j]))

pair_ = []

for i in range(m):
    for j in range(m):
        if i != j:
            if data[i] == data[j]:
                if (j, i) not in pair_:
                    pair_.append((i, j))

print(len(pair_))