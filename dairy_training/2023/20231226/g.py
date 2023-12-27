n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

is_stopped = [[False for _ in range(m)] for _ in range(n)]
is_visited = [[False for _ in range(m)] for _ in range(n)]
is_visited[1][1] = True
que= [[1, 1]]

while(que):
    h, w = que.pop()
    is_stopped[h][w] = True
    if s[h - 1][w] == ".":
        add = 1
        while(s[h - add][w] == "."):
            is_visited[h - add][w] = True
            add += 1
        add -= 1
        if not is_stopped[h - add][w]:
            que.append([h - add, w])
            is_stopped[h - add][w] = True
    if s[h + 1][w] == ".":
        add = 1
        while(s[h + add][w] == "."):
            is_visited[h + add][w] = True
            add += 1
        add -= 1
        if not is_stopped[h + add][w]:
            que.append([h + add, w])
            is_stopped[h + add][w] = True
    if s[h][w - 1] == ".":
        add = 1
        while(s[h][w - add] == "."):
            is_visited[h][w - add] = True
            add += 1
        add -= 1
        if not is_stopped[h][w - add]:
            que.append([h, w - add])
            is_stopped[h][w - add] = True
    if s[h][w + 1] == ".":
        add = 1
        while(s[h][w + add] == "."):
            is_visited[h][w + add] = True
            add += 1
        add -= 1
        if not is_stopped[h][w + add]:
            que.append([h, w + add])
            is_stopped[h][w + add] = True

ans = 0
for h in range(n):
    for w in range(m):
        if is_visited[h][w]:
            ans += 1
print(ans)