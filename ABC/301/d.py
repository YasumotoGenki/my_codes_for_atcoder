s = input()
n = int(input())

ans = 0
s_length = len(s)
# ?以外の2進数を計算
for i in range(s_length):
    if s[i] == '1':
        ans += 1 << (s_length - i - 1)

if ans > n:
    print(-1)
    exit()

# ?を左先頭から1にできるかを計算して、Nを越えないか確認
for i in range(s_length):
    if s[i] == '?':
        add_num = 1 << (s_length - i - 1)
        if ans + add_num <= n:
            ans += add_num

print(ans)