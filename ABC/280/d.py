def factorization(n):
    fact_dict = dict()
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            while temp % i == 0:
                temp //= i
                if i not in fact_dict:
                    fact_dict[i] = 1
                else:
                    fact_dict[i] += 1

    if temp != 1:
        fact_dict[1] = 1
        fact_dict[temp] = 1

    if not fact_dict:
        fact_dict[1] = 1
        fact_dict[temp] = 1

    return fact_dict

#######

k = int(input())
fact_dict = factorization(k)

ans = 0
for key in fact_dict.keys():
    if key == 1:
        continue
    count = fact_dict[key]
    i = 0
    while(count > 0):
        i += 1
        cur = key * i
        while(cur % key == 0):
            cur //= key
            count -= 1
    ans = max(ans, key * i)
print(ans)