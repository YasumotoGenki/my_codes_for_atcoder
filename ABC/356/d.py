n, m = map(int, input().split())
mod = 998244353

bin_n = bin(n)
bin_m = bin(m)

ans = 0

for i in range(len(bin_n[2:])):
    # 同じ桁を比較
    if len(bin_m) - 2 > i and bin_m[-1 - i] == "1":
        # 1の場合はNに含まれる数を計算
        base = pow(2, i) * 2
        count = (n + 1) // base * pow(2, i)
        count %= mod
        if ((n + 1) % base) - (base // 2) > 0:
            count += ((n + 1) % base) - (base // 2)
            count %= mod
        ans += count
        ans %= mod
print(ans)
