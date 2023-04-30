from math import gcd

a, b = map(int, input().split())
ans = 0

memo_table = dict()

def memo_gcd(n, m):
    global memo_table
    while(True):
        if n < m:
            n, m = m, n
        g = m
        key = str(n) + "+" + str(m)
        if key in memo_table:
            return memo_table[key]
        memo_table[key] = 
        




# while(a > 1 and b > 1):
#     g = gcd(a, b)
#     a -= g
#     b -= g
#     ans += 1

# if a > b:
#     a, b = b, a

# if a <= 0:
#     print(ans)
# elif a == 1:
#     ans += b
#     print(ans)
