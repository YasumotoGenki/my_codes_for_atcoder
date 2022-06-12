from collections import deque

n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

ax -= 1
ay -= 1
bx -= 1
by -= 1

if (ax + ay) % 2 != (bx + by) % 2:
    print(-1)
    exit()

visited_list = [[-1 for _ in range(n)] for __ in range(n)]
visited_list[ax][ay] = 0
queue = deque()
queue.append([ax, ay])

# ans = -1

# bfs
while(queue):
    x, y = queue.popleft()
    # ↗︎
    for i in range(1, min(n - x, y) + 1):
        if x + i >= n or y - i < 0 or s[x + i][y - i] == "#" or (visited_list[x + i][y - i] != -1 and visited_list[x + i][y - i] < visited_list[x][y]):
            break
        else:
            if x + i == bx and y - i == by:
                print(visited_list[x][y] + 1)
                exit()
            if visited_list[x + i][y - i] == -1 or visited_list[x + i][y - i] > visited_list[x][y] + 1:
                visited_list[x + i][y - i] = visited_list[x][y] + 1
                queue.append([x + i, y - i])
                # if x + i == bx and y - i == by:
                #     if ans == -1:
                #         ans = visited_list[x][y] + 1
                #     else:
                #         min(ans, visited_list[x][y] + 1)
    # ↘︎
    for i in range(1, min(n - x, n - y) + 1):
        if x + i >= n or y + i >= n or s[x + i][y + i] == "#" or (visited_list[x + i][y + i] != -1 and visited_list[x + i][y + i] < visited_list[x][y]):
            break
        else:
            if x + i == bx and y + i == by:
                print(visited_list[x][y] + 1)
                exit()
            if visited_list[x + i][y + i] == -1 or visited_list[x + i][y + i] > visited_list[x][y] + 1:
                visited_list[x + i][y + i] = visited_list[x][y] + 1
                queue.append([x + i, y + i])
    # ↙︎
    for i in range(1, min(x, n - y) + 1):
        if x - i < 0 or y + i >= n or s[x - i][y + i] == "#" or (visited_list[x - i][y + i] != -1 and visited_list[x - i][y + i] < visited_list[x][y]):
            break
        else:
            if x - i == bx and y + i == by:
                print(visited_list[x][y] + 1)
                exit()
            if visited_list[x - i][y + i] == -1 or visited_list[x - i][y + i] > visited_list[x][y] + 1:
                visited_list[x - i][y + i] = visited_list[x][y] + 1
                queue.append([x - i, y + i])
    # ↖︎
    for i in range(1, min(x, y) + 1):
        if x - i < 0 or y - i < 0 or s[x - i][y - i] == "#" or (visited_list[x - i][y - i] != -1 and visited_list[x - i][y - i] < visited_list[x][y]):
            break
        else:
            if x - i == bx and y - i == by:
                print(visited_list[x][y] + 1)
                exit()
            if visited_list[x - i][y - i] == -1 or visited_list[x - i][y - i] > visited_list[x][y] + 1:
                visited_list[x - i][y - i] = visited_list[x][y] + 1
                queue.append([x - i, y - i])

print(visited_list[bx][by])