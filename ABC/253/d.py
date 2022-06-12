n, a, b = map(int, input().split())

def do_gcd(a, b):
    if a == b:
        #return False
        return a

    while True:
        if a % b == 0:
            break
        else:
            a, b = b, a % b
    return b

def do_lcm(a, b, c):
    return a * b // c

asum = (n // a) * (a + n - (n % a)) // 2
bsum = (n // b) * (b + n - (n % b)) // 2
ab = do_lcm(a, b, do_gcd(a, b))
absum = (n // ab) * (ab + n - (n % ab)) // 2
nsum = n * (1 + n) // 2

print(nsum - asum - bsum + absum)