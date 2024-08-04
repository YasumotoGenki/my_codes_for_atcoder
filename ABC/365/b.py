n = int(input())
a = list(map(int, input().split()))

a_w_indices = []
for i in range(n):
    a_w_indices.append([a[i], i + 1])
a_w_indices.sort()

print(a_w_indices[-2][1])