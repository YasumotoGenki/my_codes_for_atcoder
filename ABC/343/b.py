n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    ans = []
    for j in range(n):
        if i == j:
            continue
        if a[j] == 1:
            ans.append(str(j + 1))
    print(" ".join(ans))