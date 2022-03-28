from math import ceil, floor
from decimal import Decimal

x = int(input())
mod = 998244353
que = dict()
que[x] = 1
flg = True
done = dict()

while(que):
    new_que = dict()
    for key, value in que.items():
        if key > 4:
            key = Decimal(key)
            c = ceil(key / 2)
            f = floor(key / 2)
            if c not in new_que:
                new_que[c] = value
            else:
                new_que[c] += value
            if f not in new_que:
                new_que[f] = value
            else:
                new_que[f] += value
        else:
            if key not in done:
                done[key] = value
            else:
                done[key] += value
    que = new_que

ans = 1
for key, value in done.items():
    ans *= pow(key, value, mod)
    ans %= mod
print(ans)