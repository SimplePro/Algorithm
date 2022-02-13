L, R = input().split()

if len(L) != len(R): print(0)
elif L[0] != R[0]: print(0)
else:
    cnt = 0

    if L[0] == '8': cnt += 1

    for i in range(1, len(L)):
        if L[i] != R[i]: break
        if L[i] == '8': cnt += 1

    print(cnt)