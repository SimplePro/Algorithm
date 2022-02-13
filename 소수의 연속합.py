N = int(input())

is_prime = [0, 0]  + [1]*(N-1)
prime_number = []

for i in range(2, N+1):
    if is_prime[i]:
        prime_number.append(i)

        for j in range(2*i, N+1, i):
            is_prime[j] = 0

start, end = 0, 0
tmp_sum = 0
result = 0

while True:
    if tmp_sum == N:
        result += 1
        tmp_sum -= prime_number[start]
        start += 1

    elif end < len(prime_number) and tmp_sum < N:
        tmp_sum += prime_number[end]
        end += 1
    
    elif start < len(prime_number):
        tmp_sum -= prime_number[start]
        start += 1

    if start == end: break

print(result)