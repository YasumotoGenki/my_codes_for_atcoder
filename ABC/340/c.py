from decimal import Decimal
from math import ceil, floor
n = int(input())
que = [n]
memo = dict()

def dfs(num: int):
    global memo
    value = num
    c = ceil(Decimal(num) / 2)
    f = floor(Decimal(num) / 2)

    if c > 1:
        if c not in memo:
            memo[c] = dfs(c)
        value += memo[c]
    if f > 1:
        if f not in memo:
            memo[f] = dfs(f)
        value += memo[f]
     
    return value

ans = dfs(n)    
print(ans)

# count = 0
# while(que):
#     value = que.pop()
#     count += value
#     c = ceil(value / 2)
#     f = floor(value / 2)
#     if c > 1:
#         que.append(c)
#     else:
#         memo[]
#     if f > 1:
#         que.append(f)

# print(count)