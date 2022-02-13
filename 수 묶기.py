N = int(input())
positive = []
negative = []
result = 0

for _ in range(N):
    n = int(input())
    if n > 1: positive.append(n)
    elif n == 1: result += 1
    else: negative.append(n)

positive.sort(key=lambda x: -x)
negative.sort()

# 0, 양수 -> 더하기
# 0, 음수 -> 곱하기
# 양수, 양수 -> 곱셈
# 음수, 음수 -> 곱셈

for i in range(0, len(positive) - (len(positive)%2), 2):
    result += positive[i]*positive[i+1]

for i in range(0, len(negative) - (len(negative)%2), 2):
    result += negative[i]*negative[i+1]

if len(positive) % 2: result += positive[-1]
if len(negative) % 2: result += negative[-1]

print(result)