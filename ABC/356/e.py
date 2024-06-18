n = int(input())
a = list(map(int, input().split()))
a.sort()

max_a = max(a)
s = [0 for i in range(max_a + 1)]
count = 0
pre = 0
for item_a in a:
    if pre != item_a:
        for i in range(pre + 1, item_a):
            s[i] = count 
    count += 1
    s[item_a] = count
    pre = item_a

idx = 0
ans = 0

from collections import Counter
counter_a = Counter(a)
for key in sorted(counter_a.keys()):
    if key == max_a:
        ans += counter_a[key] * (counter_a[key] - 1) // 2
    else:
        if counter_a[key] > 1:
            ans += counter_a[key] * (counter_a[key] - 1) // 2
        pre_count = s[key]
        end_flg = False
        for i, j in enumerate(range(key + key - 1, 100_000_000_000_000, key)):
            if j > max_a:
                count = s[-1]
                end_flg = True
            else:
                count = s[j]
            ans += (i + 1) * (count - pre_count) * counter_a[key]
            pre_count = count
            if end_flg:
                break
print(ans)