import sys
sys.setrecursionlimit(10 ** 7)

from collections import deque

n = int(input())
s = input()
t = input()


def str2value(letters):

    value = int(letters, 3)
    return value

INF = 10 ** 20
# dp定義
# 3進数で表現
# 0: ".", 1: "W", 2: "B"
dp = [INF for _ in range(3 ** (n + 2) + 1)]

# 今の状態に0を代入
s += ".."
s = s.replace(".", "0")
s = s.replace("W", "1")
s = s.replace("B", "2")
idx = str2value(s)
dp[idx] = 0
que = deque([[idx, s]])


t += ".."
t = t.replace(".", "0")
t = t.replace("W", "1")
t = t.replace("B", "2")
goal_idx = str2value(t)

if dp[goal_idx] == 0:
    print(0)
    exit()

if t.count('1') != s.count('1'):
    print(-1)
    exit()

# queを作って、更新したらqueに入れる
while(que):
    idx, current_str = que.popleft()
    cost = dp[idx]
    piriod_idx = current_str.index("00")
    for i in range(n + 1):
        if abs(i - piriod_idx) < 2:
            continue
        small_idx = min(i, piriod_idx)
        large_idx = max(i, piriod_idx)
        new_str = current_str[:small_idx] + current_str[large_idx:large_idx + 2] + current_str[small_idx + 2:large_idx] + current_str[small_idx:small_idx+2] + current_str[large_idx + 2:]
        new_idx = str2value(new_str)
        if dp[new_idx] > cost + 1:
            dp[new_idx] = cost + 1
            que.append([new_idx, new_str])
            if new_idx == goal_idx:
                print(cost + 1)
                exit()
    
print(-1)