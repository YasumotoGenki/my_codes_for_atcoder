n, l, r =  map(int, input().split())
a = list(map(int, input().split()))

ans = []
for i in range(n):
    if a[i] > r:
        ans.append(str(r))
    elif l <= a[i] <= r:
        ans.append(str(a[i]))
    else:
        ans.append(str(l))
print(" ".join(ans))