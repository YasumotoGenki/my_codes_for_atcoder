n = int(input())
original_set = set()
score_list = []
for i in range(n):
    s, t = map(str, input().split())
    t = int(t)
    if s not in original_set:
        original_set.add(s)
        score_list.append([t, -i - 1])

score_list.sort(reverse=True)
print(-score_list[0][1])