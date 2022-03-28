a, b, c, d = map(int, input().split())
if a < c:
    ans = "Takahashi"
elif a == c and b <= d:
    ans = "Takahashi"
else:
    ans = "Aoki"
print(ans)