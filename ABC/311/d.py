n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

ans = set()
stopped = set()

def bfs(current):
    global ans
    global stopped
    next_list = []
    for plus_minus in [-1, 1]:
        for idx in [0, 1]:
            for i in range(1, 200):
                if idx == 0:
                    if 0 <= current[idx] + i * plus_minus < n and s[current[idx] + i * plus_minus][current[1]] == ".":
                        ans.add((current[idx] + i * plus_minus, current[1]))
                        if 0 > current[idx] + (i + 1) * plus_minus or current[idx] + (i + 1) * plus_minus == n or s[current[idx] + (i + 1) * plus_minus][current[1]] == "#":
                            if (current[idx] + i * plus_minus, current[1]) not in stopped:
                                stopped.add((current[idx] + i * plus_minus, current[1]))
                                next_list.append((current[idx] + i * plus_minus, current[1]))
                            break
                    else:
                        break
                if idx == 1:
                    if 0 <= current[idx] + i * plus_minus < m and s[current[0]][current[idx] + i * plus_minus] == ".":
                        ans.add((current[0], current[idx] + i * plus_minus))
                        if 0 > current[idx] + (i + 1) * plus_minus or current[idx] + (i + 1) * plus_minus == m or s[current[0]][current[idx] + (i + 1) * plus_minus] == "#":
                            if (current[0], current[idx] + i * plus_minus) not in stopped:
                                stopped.add((current[0], current[idx] + i * plus_minus))
                                next_list.append((current[0], current[idx] + i * plus_minus))
                            break
                    else:
                        break
    return next_list

# (1,1)スタート
ans.add((1, 1))
stopped.add((1, 1))
que = [(1, 1)]

while(que):
    current = que.pop()
    next_list = bfs(current=current)
    que += next_list

print(len(ans))