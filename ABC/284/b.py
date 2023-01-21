n = int(input())
s = input()


for i in range(1, n):
    ans = 0
    for j in range(n - i):
        if s[j] != s[j + i]:
            ans = j + 1
        else:
            break
    print(ans)