n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

relationship_dict = dict()
for i in range(m):
    a[i] -= 1
    b[i] -= 1
    if a[i] not in relationship_dict:
        relationship_dict[a[i]] = set()
    relationship_dict[a[i]].add(b[i])
    if b[i] not in relationship_dict:
        relationship_dict[b[i]] = set()
    relationship_dict[b[i]].add(a[i])    

candidate_ans = [None for _ in range(n)]
que = []
que.append(a[i])
done = set()
a_idx = 0

while(que):
    q = que.pop()
    for r in relationship_dict[q]:
    # a_i, b_i がすでにあるかをチェック
        # とちらもない場合
        if candidate_ans[q] is None and candidate_ans[r] is None:
            if q == r:
                print("No")
                exit()
            candidate_ans[q] = 1
            candidate_ans[r] = 0
            que.append(r)
        # 片方がある場合
        elif candidate_ans[q] is None:
            candidate_ans[q] = 1 if candidate_ans[r] == 0 else 0
            que.append(q)
        elif candidate_ans[r] is None:
            candidate_ans[r] = 1 if candidate_ans[q] == 0 else 0
            que.append(r)
        # 両方ある場合
        else:
            if candidate_ans[r] != candidate_ans[q]:
                pass
            else:
                print("No")
                exit()

    done.add(q)
    while(not que and a_idx < m):
        if a[a_idx] not in done:
            que.append(a[a_idx])
        a_idx += 1
print("Yes")