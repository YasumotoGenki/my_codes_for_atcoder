from collections import defaultdict

n, k = map(int, input().split())
s = input()
mod = 998244353

# dp[n][key] = num
dp = [defaultdict(int) for _ in range(n + 1)]
dp[0][""] = 1


def is_kaibun(letters):
    flg = True
    for i in range(len(letters) // 2):
        if letters[i] != letters[-1 -i]:
            flg = False
            break
    return flg


for i in range(n):
    for key, value in dp[i].items():
        if len(key) < k:
            idx = 0
        else:
            idx = 1
        
        if s[i] == 'A':
            next_words = [key[idx:] + 'A']
        elif s[i] == 'B':
            next_words = [key[idx:] + 'B']
        elif s[i] == '?':
            next_words = [key[idx:] + 'A', key[idx:] + 'B']
        for next_word in next_words:
            if len(next_word) == k:
                if is_kaibun(next_word):
                    continue
            dp[i + 1][next_word] += value
            dp[i + 1][next_word] %= mod

ans = 0
for key, value in dp[-1].items():
    ans += value
    ans %= mod
print(ans)