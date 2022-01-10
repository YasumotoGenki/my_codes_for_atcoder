q = int(input())

N = 1048576

pointer = dict()
values = dict()

for i in range(q):
    t, x = map(int, input().split())
    idx = x % N
    if t == 1:
        if idx in values:
            p_idx = pointer[idx]
            change_list= []
            change_list.append(idx)
            while(True):
                if p_idx not in values:
                    change_list.append(p_idx)
                    pp_idx = p_idx + 1
                    if pp_idx > N - 1:
                        pp_idx = 0
                    for change_id in change_list:
                        pointer[change_id] = pp_idx
                    break
                else:
                    change_list.append(p_idx)
                    p_idx = pointer[p_idx]
            values[p_idx] = x
        else:
            values[idx] = x
            p_idx = idx + 1
            if p_idx > N - 1:
                p_idx = 0
            pointer[idx] = p_idx
    else:
        if idx not in values:
            print(-1)
        else:
            print(values[idx])

