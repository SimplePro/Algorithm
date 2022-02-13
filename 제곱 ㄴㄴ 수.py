min_, max_ = map(int, input().split())

square_n = 2
check = set()

for i in range(min_, max_+1):
    check.add(i)

while square_n**2 <= max_:
    square = square_n ** 2
    j = min_ // square

    if min_ % square: j += 1

    while square * j <= max_:
        if square*j in check: check.remove(square*j)
        j += 1

    square_n += 1

print(len(check))