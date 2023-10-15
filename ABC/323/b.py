n = int(input())
match_result_list = [] # [win_count, - player_idx]
for i in range(n):
    match_result = list(input())
    win_count = 0
    for item in match_result:
        if item == "o":
            win_count += 1
    match_result_list.append([win_count, -i])

match_result_list.sort(reverse=True)
ans = []
for i in range(n):
    ans.append(-match_result_list[i][1] + 1)
print(*ans)