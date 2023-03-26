n, m = map(int, input().split())
xy = []
small_2_big_list = [[] for _ in range(n)]
big_count_list = [0 for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    small_2_big_list[x].append(y)
    big_count_list[y] += 1

que = []
for i in range(n):
    if big_count_list[i] == 0:
        que.append(i)
if len(que) == 0 or len(que) > 1:
    print("No")
    exit()

m_count = m
indices = []
while(True):
    small_i = que.pop()
    indices.append(small_i)
    for big_i in small_2_big_list[small_i]:
        big_count_list[big_i] -= 1
        m_count -= 1
        if big_count_list[big_i] == 0:
            que.append(big_i)
    if m_count == 0:
        small_i = que.pop()
        indices.append(small_i)
        break
    elif len(que) == 0 or len(que) > 1:
        print("No")
        exit()

ans = [0 for _ in range(n)]

if len(indices) < n:
    print("No")
    exit()
for i in range(n):
    ans[indices[i]] = i + 1

if 0 in ans:
    print("No")
else:
    print("Yes")
    print(*ans)