from collections import deque

n = int(input())
s = []
player_positions = []
for i in range(n):
    line = input()
    if "P" in line:
        ridx = line.rindex("P")
        lidx = line.index("P")
        player_positions.append([i, lidx])
        if lidx != ridx:
            player_positions.append([i, ridx])
    s.append(line)


done = [[[[False for _ in range(n)]  for _ in range(n)] for _ in range(n)] for _ in range(n)]
p1_x, p1_y = player_positions[0]
p2_x, p2_y = player_positions[1]
done[p1_x][p1_y][p2_x][p2_y] = True

que = deque([[0, p1_x, p1_y, p2_x, p2_y]])
distance = [[1, 0], [0, 1], [-1, 0], [0, -1]]

while(que):
    cost, p1_x, p1_y, p2_x, p2_y = que.popleft()
    if p1_x == p2_x and p1_y == p2_y:
        print(cost)
        exit()
    for dx, dy in distance:
        next_p1_x = p1_x + dx
        next_p1_y = p1_y + dy
        next_p2_x = p2_x + dx
        next_p2_y = p2_y + dy

        if next_p1_x < 0 or next_p1_x >= n or next_p1_y < 0 or next_p1_y >= n or s[next_p1_x][next_p1_y] == "#":
            next_p1_x = p1_x
            next_p1_y = p1_y
        if next_p2_x < 0 or next_p2_x >= n or next_p2_y < 0 or next_p2_y >= n or s[next_p2_x][next_p2_y] == "#":
            next_p2_x = p2_x
            next_p2_y = p2_y

        if not done[next_p1_x][next_p1_y][next_p2_x][next_p2_y]:
            que.append([cost + 1, next_p1_x, next_p1_y, next_p2_x, next_p2_y])
            done[next_p1_x][next_p1_y][next_p2_x][next_p2_y] = True

print(-1)