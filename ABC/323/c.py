n, m = map(int, input().split())
a = list(map(int, input().split()))
s = []
score_and_player_idx_list = [] # [score, player_idx]
player_score_list = []
for player_idx in range(n):
    input_line = input()
    s.append(input_line)
    # 現在の点数を計算
    current_player_score = 0
    for j in range(m):
        if input_line[j] == "o":
            current_player_score += a[j]
    current_player_score += player_idx + 1
    score_and_player_idx_list.append([current_player_score, player_idx])   
    player_score_list.append(current_player_score) 

score_and_player_idx_list.sort(reverse=True)

# aの要素とidxをソートした配列を用意
sorted_a_and_idx_list = [[item_a, idx] for idx, item_a in enumerate(a)]
sorted_a_and_idx_list.sort(reverse=True)

for i in range(n):
    # 自分自身であるかどうかの判定
    if score_and_player_idx_list[0][1] == i:
        # 自分の場合、２番目の人が同じ点数かどうかチェック
        if score_and_player_idx_list[0][0] == score_and_player_idx_list[1][0]:
            print(1)
        else:
            print(0)
        continue
    # 自信ではない場合、他の最も得点が高い人との差を埋めるまで、得点が高く未解答の問題を貪欲的に加算し、問題数をカウント
    ans = 0
    plus_score = 0
    sorted_a_idx = 0
    while(player_score_list[i] + plus_score <= score_and_player_idx_list[0][0]):
        idx = sorted_a_and_idx_list[sorted_a_idx][1]
        if s[i][idx] == "x":
            plus_score += a[idx]
            ans += 1
        sorted_a_idx += 1
    print(ans)