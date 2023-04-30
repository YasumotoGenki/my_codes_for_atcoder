n = int(input())
a = list(map(int, input().split()))

direct_list = [[] for _ in range(n)]

done_set = set()
ans = set()

for i in range(n):
    if i in done_set:
        continue    
    visited_path_set = set()
    visited_path_list = []
    node_2_idx_dict = dict()
    count = 0
    cur_node = i
    while(True):
        # cur_nodeがこれまでに訪れたことがないか確認
        if cur_node in visited_path_set:
            # ループ発見
            idx = node_2_idx_dict[cur_node]
            ans |= set(visited_path_list[idx:])
            break
        if cur_node in done_set:
            break
        # 訪れたことがない場合はパス集合、リストに追加
        visited_path_set.add(cur_node)
        visited_path_list.append(cur_node)
        node_2_idx_dict[cur_node] = count
        count += 1
        # done_setに追加
        done_set.add(cur_node)
        # next_nodeを求める
        next_node = a[cur_node] - 1
        # cur_nodeをnext_nodeに
        cur_node = next_node
print(len(ans))