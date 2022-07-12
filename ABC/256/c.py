hw = list(map(int, input().split()))

ans = 0
for top_left_num in range(1, hw[3] - 1):
    for top_middle_num in range(1, hw[3] - top_left_num):
        top_right_num = hw[3] - top_left_num - top_middle_num
        for middle_left_num in range(1, hw[4] - 1):
            for middle_middle_num in range(1, hw[4] - middle_left_num):
                middle_right_num = hw[4] - middle_left_num - middle_middle_num
                for bottom_left_num in range(1, hw[5] - 1):
                    for bottom_middle_num in range(1, hw[5] - bottom_left_num):
                        bottom_right_num = hw[5] - bottom_left_num - bottom_middle_num
                        if top_left_num + middle_left_num + bottom_left_num == hw[0] and top_middle_num + middle_middle_num + bottom_middle_num == hw[1] and top_right_num + middle_right_num + bottom_right_num == hw[2]:
                            ans += 1
print(ans)