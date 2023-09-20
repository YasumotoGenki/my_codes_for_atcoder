n, m = map(int, input().split())
looking_dict_list = [dict() for _ in range(n)]
for _ in range(m):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    looking_dict_list[a][b] = [x, y]
    looking_dict_list[b][a] = [-x, -y]

ans = [None for _ in range(n)]
ans[0] = [0, 0]
que = [0]
while(que):
    current_person = que.pop()
    for next_person in looking_dict_list[current_person].keys():
        if ans[next_person] is None:
            x, y = looking_dict_list[current_person][next_person]
            ans[next_person] = [ans[current_person][0] +  x, ans[current_person][1] + y]
            que.append(next_person)

for i in range(n):
    if ans[i] is None:
        print("undecidable")
    else:
        print(*ans[i])
