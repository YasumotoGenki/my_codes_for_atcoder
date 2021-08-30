import copy
import sys
sys.setrecursionlimit(200000)

n, m = map(int, input().split())

k = []
a = []

for i in range(m):
    cur_k = int(input())
    k.append(cur_k)
    cur_a = list(map(int, input().split()))[::-1]
    a.append(cur_a)

set_left_indices = set([i for i in range(m)])

while(True):
    initial_num_set = set()
    num_to_index_dict = dict()
    flg = [False]

    def recheck_num(cur_num, cur_idx):
        if cur_num in initial_num_set:
            flg[0] = True
            pre_idx = num_to_index_dict[cur_num]
            # 除外
            a[pre_idx].pop()
            k[pre_idx] -= 1
            if k[pre_idx] == 0:
                set_left_indices.remove(pre_idx)
            # 除外
            a[cur_idx].pop()
            k[cur_idx] -= 1
            if k[cur_idx] == 0:
                set_left_indices.remove(cur_idx)

            if cur_idx in set_left_indices:
                next_num = a[cur_idx][-1]
                recheck_num(next_num, cur_idx)
            
            if pre_idx in set_left_indices:
                next_num = a[pre_idx][-1]
                recheck_num(next_num, pre_idx)
        else:
            initial_num_set.add(cur_num)
            num_to_index_dict[cur_num] = cur_idx

    pre_set_left_indices = copy.deepcopy(set_left_indices)
    for idx in pre_set_left_indices:
        if idx in set_left_indices:
            num = a[idx][-1]
            recheck_num(num, idx)
        
    if len(set_left_indices) == 0:
        print("Yes")
        exit()
    if not flg[0]:
        print("No")
        exit()
