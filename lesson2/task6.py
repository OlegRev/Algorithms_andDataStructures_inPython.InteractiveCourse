def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


def gcd2(m, n):
    if n == 0:
        return m
    return gcd2(n, m % n)


def gcd3(m, n):
    while n != 0:
        m, n = n, m % n
    return m


m, n = 540, 24458732646
sepr = f"{'**' * 10}"
print(gcd(m, n))
print(sepr)
print(gcd2(m, n))
print(sepr)
print(gcd3(m, n))
