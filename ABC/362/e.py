from bisect import bisect_right

n = int(input())
a = list(map(int, input().split()))

mod = 998244353

# 1回目カウントはn
ans_list = [n]
if n == 1:
    print(n)
    exit()
# 2回目カウントして、各要素にdiffがどれだけくっついているかを調べる
diff_list = [dict() for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        diff = a[j] - a[i]
        if diff not in diff_list[j]:
            diff_list[j][diff] = 0
        diff_list[j][diff] += 1

ans_list.append(n * (n - 1) // 2)

# num2idx
num2idx_dict = dict()
for i in range(n):
    if a[i] not in num2idx_dict:
        num2idx_dict[a[i]] = []
    num2idx_dict[a[i]].append(i)

# ホップ数分ループ（n）
for i in range(1, n - 1):
    # diff_listを作る
    new_diff_list = [dict() for _ in range(n)]
    # 要素ごとに次のホップができるのかを調査
    for j in range(i, n):
        for diff, count in diff_list[j].items():
            search_value = a[j] + diff
            if search_value in num2idx_dict:
                idx = bisect_right(num2idx_dict[search_value], j)
                if len(num2idx_dict[search_value]) == idx:
                    continue
                for k in num2idx_dict[search_value][idx:]:
                    if diff not in new_diff_list[k]:
                        new_diff_list[k][diff] = 0
                    new_diff_list[k][diff] += count

    total = 0
    for j in range(i, n):
        for key, value in new_diff_list[j].items():
            total += value
            total %= mod
    ans_list.append(total)        
    diff_list = new_diff_list

print(*ans_list)