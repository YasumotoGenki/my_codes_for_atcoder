n = int(input())
a = list(map(int, input().split()))

base_list = [0 for i in range(4)]
ans = 0
for i in range(n):
    base_list[0] += 1
    for j in range(3, -1, -1):
        if j + a[i] >= 4:
            ans += base_list[j]
        else:
            base_list[j + a[i]] += base_list[j]
        base_list[j] = 0
print(ans)