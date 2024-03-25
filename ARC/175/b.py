n, a, b = map(int, input().split())
s = list(input())

diff = (s.count("(") - s.count(")")) // 2

reverse_index = -1
end_kakko_count = 0
count_start_kakko = 0
count_end_kakko = 0
ans = 0
for i in range(2 * n):
    current_kakko = s[i]
    if current_kakko == ")":
        if count_start_kakko - count_end_kakko <= 0:
            if b * 2 <= a:
                ans += b
                diff += 1
            elif diff < 0:
                ans += b
                diff += 1
            else: # "("が多いか同じ数ある場合
                flg = True
                while(flg):
                    searching_kakko = s[reverse_index]
                    if searching_kakko == "(":
                        end_kakko_count -= 1
                    else:
                        end_kakko_count += 1
                    if end_kakko_count < 0:
                        ans += a
                        s[i], s[reverse_index] = s[reverse_index], s[i]
                        flg = False
                        end_kakko_count += 1
                    reverse_index -= 1
            count_start_kakko += 1
        else:
            count_end_kakko += 1
    else: # "("
        if diff > 0:
            if count_start_kakko >= n:
                ans += b
                diff -= 1
                count_end_kakko += 1
            else:
                count_start_kakko += 1
        else:
            count_start_kakko += 1
print(ans)