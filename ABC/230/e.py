n = int(input())
div_num = 1
div_set = set()

ans = 0

while(div_num <= n):
    cur_div = n // div_num
    if (n + 1) // div_num == cur_div:
        lim_div = n // cur_div
        if lim_div > n:
            lim_div = n
        ans += (lim_div - div_num + 1) * cur_div
        div_num = lim_div + 1
    else:
        ans += cur_div
        div_num += 1
print(ans)