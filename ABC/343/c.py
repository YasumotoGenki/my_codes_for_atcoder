n = int(input())

for i in range(1, 1000002):
    if i ** 3 > n:
        max_k = i - 1
        break

def judge_kaibun(num):
    judge = True
    str_num = str(num)
    length = len(str_num)
    half_len = length // 2
    for i in range(half_len):
        if str_num[i] != str_num[-i-1]:
            judge = False
    return judge

for i in range(max_k, -1, -1):
    j = i ** 3
    if judge_kaibun(j):
        print(j)
        exit()