n, m = map(int, input().split())

n_factorial = 1
m_factorial = 1

for i in range(n, n-m, -1):
    n_factorial *= i

for i in range(m, 1, -1):
    m_factorial *= i

print(n_factorial // m_factorial)
