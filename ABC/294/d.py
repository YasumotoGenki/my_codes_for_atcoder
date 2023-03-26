from collections import deque

n, q = map(int, input().split())

is_called_by_q2 = [False] * n
called_idx = 1
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        pass
    elif query[0] == 2:
        already_called_idx = query[1] - 1
        is_called_by_q2[already_called_idx] = True
    else:
        while(True):
            if is_called_by_q2[called_idx - 1]:
                called_idx += 1
                continue
            else:
                print(called_idx)
                break
