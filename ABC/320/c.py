from itertools import permutations

m = int(input())
s = []

for i in range(3):
    s.append(list(input()))

# 同一の文字があるか判定
candidate_numbers = set(s[0]) & set(s[1]) & set(s[2])
if not candidate_numbers:
    print(-1)
    exit()

ans = 1000000
# ３つのリールにある文字を走査
for candidate_num in candidate_numbers:
    # permiutationで回して、1->2->3, 1->3->2のように全ての順を検証
    for slot_indices in permutations([0, 1, 2], 3):
        current_count = 0
        current_time = 0
        # 番号が現れるまで何秒かかるかを加算
        for i, s_idx in enumerate(slot_indices):
            current_idx = current_time % m
            # 現在のidx以降であるか確認
            if candidate_num in s[s_idx][current_idx:]:
                count = s[s_idx][current_idx:].index(candidate_num)
                current_time += count
            else:
                current_time += m - (current_time % m)
                count = s[s_idx].index(candidate_num)
                current_time += count
            if i != 2:
                current_time += 1
        ans = min(ans, current_time)
print(ans)