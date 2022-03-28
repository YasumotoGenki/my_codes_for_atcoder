def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

for i in range(a, b + 1):
    flg = True
    for j in range(c, d + 1):
        if is_prime(i + j):
            flg = False
    if flg:
        print("Takahashi")
        exit()
print("Aoki")