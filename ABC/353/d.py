n = int(input())
a = list(map(int, input().split()))

digit_counter = dict()

for i in range(n):
    digit = len(str(a[i]))
    if digit not in digit_counter:
        digit_counter[digit] = 0
    digit_counter[digit] += 1

s = [0]
for i in range(n):
    s.append(s[-1] + a[i])

ans = 0
mod = 998244353

for i in range(n - 1):
    # 下の数（y）を累積話で計算
    ans += s[-1] - s[i + 1]
    ans %= mod

    # 残りの桁カウント調整
    digit = len(str(a[i]))
    digit_counter[digit] -= 1

    # 上の数（x）を桁数から計算
    for digit, value in digit_counter.items():
        ans += (10 ** digit) * a[i] * value
        ans %= mod

print(ans)