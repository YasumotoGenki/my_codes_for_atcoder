def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            while temp % i == 0:
                temp //= i
            arr.append(i)

    if temp != 1:
        arr.append(1)
        arr.append(n)

    if not arr:
        arr.append(1)
        arr.append(n)

    return arr

n = int(input())
a = list(map(int, input().split()))

count_2_div_list = [0 for _ in range(n)]
count_3_div_list = [0 for _ in range(n)]
pre_fact = None

for i, item_a in enumerate(a):
    count_2_div = 0
    count_3_div = 0
    while(item_a // 2 > 0 and item_a % 2 == 0):
        count_2_div += 1
        item_a //= 2
    while(item_a // 3 > 0 and item_a % 3 == 0):
        count_3_div += 1
        item_a //= 3
    if pre_fact is None:
        pre_fact = factorization(item_a)
        count_2_div_list[i] += count_2_div
        count_3_div_list[i] += count_3_div
    else:
        if pre_fact == factorization(item_a):
            count_2_div_list[i] += count_2_div
            count_3_div_list[i] += count_3_div
            continue
        else:
            print(-1)
            exit()
ans = sum(count_2_div_list) - n * min(count_2_div_list) \
      + sum(count_3_div_list) - n * min(count_3_div_list)
print(ans)
    