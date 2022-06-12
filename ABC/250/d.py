from traceback import print_tb


n = int(input())

tf = [True for _ in range(10 ** 6 + 1)]
tf[0] = False
tf[1] = False

for i in range(2, 10 ** 6 + 1):
    j = 2
    while(i * j < 1000000 + 1):
        tf[i * j] = False
        j += 1

prime_num_list = []
for i in range(2, 10 ** 6 + 1):
    if tf[i]:
        prime_num_list.append(i)

prime_num_list.reverse()

ans = 0
for i, q in enumerate(prime_num_list):
    for j in range(len(prime_num_list) - 1, i, -1):
        p = prime_num_list[j]
        if p * (q ** 3) > n:
            break
        else:
            ans += 1
print(ans)