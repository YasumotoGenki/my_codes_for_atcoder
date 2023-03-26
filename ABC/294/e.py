l, n1, n2 = map(int, input().split())

n1_vl_list = []
for i in range(n1):
    n1_vl_list.append(list(map(int, input().split())))
n2_vl_list = []
for i in range(n2):
    n2_vl_list.append(list(map(int, input().split())))

cur_above_element, cur_bottom_element = n1_vl_list[0][0], n2_vl_list[0][0]
n1_idx, above_left_idx, above_right_idx = 1, 0, n1_vl_list[0][1]
n2_idx, bottom_left_idx, bottom_right_idx = 1, 0, n2_vl_list[0][1]
ans = 0
# 要素が一致しているかを比較
if cur_above_element == cur_bottom_element:
    # 一致している場合は一致している数を計算してansに加算
    ans += min(above_right_idx, bottom_right_idx) - max(above_left_idx, bottom_left_idx)

for i in range(n1 + n2 - 2):
    # n1, n2の小さい方のidxを上げる
    if above_right_idx <= bottom_right_idx:
        above_left_idx = above_right_idx + 1
        above_right_idx += n1_vl_list[n1_idx][1]
        cur_above_element = n1_vl_list[n1_idx][0]
        n1_idx += 1
    else:
        bottom_left_idx = bottom_right_idx + 1
        bottom_right_idx += n2_vl_list[n2_idx][1]
        cur_bottom_element = n2_vl_list[n2_idx][0]
        n2_idx += 1
    # 要素が一致しているかを比較
    if cur_above_element == cur_bottom_element:
        # 一致している場合は一致している数を計算してansに加算
        ans += min(above_right_idx, bottom_right_idx) - max(above_left_idx, bottom_left_idx) + 1

print(ans)