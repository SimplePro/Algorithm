a, b, c = map(int, input().split())

def power(n, k):
    if k == 0: return 1

    temp = power(n, k//2)
    result = (temp * temp) % c

    if k % 2 == 1: result = (result * n) % c
    return result

print(power(a, b))
