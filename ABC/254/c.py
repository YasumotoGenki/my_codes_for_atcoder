from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))
sorted_a = sorted(a)

for i in range(k):
    if Counter(a[i::k]) == Counter(sorted_a[i::k]):
        pass
    else:
        print("No")
        exit()
print("Yes")