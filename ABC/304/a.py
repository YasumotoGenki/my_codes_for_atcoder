n = int(input())
min_val, min_idx = 10 ** 10, 0
list_s = []
for i in range(n):
    s, a = map(str, input().split())
    a = int(a)
    if min_val > a:
        min_val = a
        min_idx = i
    list_s.append(s)

ans = list_s[min_idx:] + list_s[:min_idx]
for item in ans:
    print(item)