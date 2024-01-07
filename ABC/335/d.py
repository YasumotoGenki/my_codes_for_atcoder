import sys
sys.setrecursionlimit(100000)

n = int(input())
center_cell = [(n + 1) // 2 - 1, (n + 1) // 2 - 1]
ans = [[None for _ in range(n)] for _ in range(n)]
ans[(n + 1) // 2 - 1][(n + 1) // 2 - 1] = "T"
ans[0][0] = "1"
count = 1

def explore(current_cell, current_command):
    global n
    global ans
    global center_cell
    global count

    x, y = current_cell
    if current_command == "D":
        if x + 1 < n and ans[x + 1][y] is None:
            count += 1
            ans[x + 1][y] = str(count)
            current_cell = [x + 1, y]
        else:
            current_command = "R"
    elif current_command == "U":
        if x - 1 >= 0 and ans[x - 1][y] is None:
            count += 1
            ans[x - 1][y] = str(count)
            current_cell = [x - 1, y]
        else:
            current_command = "L"
    elif current_command == "L":
        if y - 1 >= 0 and ans[x][y - 1] is None:
            count += 1
            ans[x][y - 1] = str(count)
            current_cell = [x, y - 1]
        else:
            current_command = "D"
    elif current_command == "R":
        if y + 1 < n and ans[x][y + 1] is None:
            count += 1
            ans[x][y + 1] = str(count)
            current_cell = [x, y + 1]
        else:
            current_command = "U"
    if count == n ** 2 - 1:
        return
    explore(current_cell, current_command)

explore([0, 0], "D")
for i in range(n):
    print(" ".join(ans[i]))