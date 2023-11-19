n, m = map(int, input().split())
a = list(map(int, input().split()))

candidate_2_count_dict = dict()
for i in range(1, n + 1):
    candidate_2_count_dict[i] = 0

for i in range(m):
    candidate_2_count_dict[a[i]] += 1
    if i == 0:
        ans = [a[i], 1]
    else:
        if candidate_2_count_dict[a[i]] > ans[-1]:
            ans = [a[i], candidate_2_count_dict[a[i]]]
        elif candidate_2_count_dict[a[i]] == ans[-1] and a[i] < ans[0]:
            ans = [a[i], ans[-1]]
    print(ans[0])