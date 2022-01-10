k = int(input())

if k == 1:
    print(2)
    exit()

digits = 1
num_count = 1

while(num_count < k):
    digits += 1
    num_count += 2 ** (digits - 1)

ans = '2'
pre_num_count = num_count - 2 ** (digits - 1)

for i in range(1, digits):
    possible_num_comb_half = (num_count - pre_num_count) // 2
    if possible_num_comb_half >= k - pre_num_count:
        ans += '0'
        num_count -= possible_num_comb_half
    else:
        ans += '2'
        pre_num_count += possible_num_comb_half

print(ans)