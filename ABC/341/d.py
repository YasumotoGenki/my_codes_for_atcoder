n, m, K = map(int, input().split())

def factorization(n):
    fact_dict = dict()
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            fact_dict[i] = cnt

    if temp!=1:
        fact_dict[temp] = 1

    if len(fact_dict) == 0:
        fact_dict[n] = 1

    return fact_dict

# 素因数分解
n_fact_dict = factorization(n)
m_fact_dict = factorization(m)

n_not_overlap = 1
m_not_overlap = 1
# お互い持たない素数をかけた値を求める
for k, v in n_fact_dict.items():
    if k not in m_fact_dict:
        n_not_overlap *= k ** v
    else:
        if v - m_fact_dict[k] > 0:
            n_not_overlap *= k ** (v - m_fact_dict[k])

for k, v in m_fact_dict.items():
    if k not in n_fact_dict:
        m_not_overlap *= k ** v
    else:
        if v - n_fact_dict[k] > 0:
            m_not_overlap *= k ** (v - n_fact_dict[k])

# 2分探索
left = 0
right = 10 ** 20

while(right - left > 1):
    middle = (left + right) // 2
    n_count = middle // n
    n_count -= (n_count // m_not_overlap)
    m_count = middle // m
    m_count -= (m_count // n_not_overlap)
    if n_count + m_count >= K:
        right = middle
    else:
        left = middle

print(right)