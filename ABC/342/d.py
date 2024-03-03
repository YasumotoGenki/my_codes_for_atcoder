from collections import Counter
from scipy.special import comb

def factorization(n):
    tmp_arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            tmp_arr.append([i, cnt])

    if temp!=1:
        tmp_arr.append([temp, 1])

    if tmp_arr==[]:
        tmp_arr.append([n, 1])

    fact_value = 1
    for fact, value in tmp_arr:
        if value % 2 != 0:
            fact_value *= fact
    return fact_value

n = int(input())
a = list(map(int, input().split()))
counter_a = Counter(a)
counter_divisors = dict()
ans = 0
for k, v in counter_a.items():
    if k == 0:
        ans += (n - v) * v
        if v >= 2:
            ans += comb(v, 2, exact=True)
    else:
        fact_value = factorization(k)
        if fact_value not in counter_divisors:
            counter_divisors[fact_value] = 0
        counter_divisors[fact_value] += v
for k, v in counter_divisors.items():
    if v >= 2:
        ans += comb(v, 2)
print(int(ans))

