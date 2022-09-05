n = int(input())
p = list(map(int, input().split()))
tf_list = []

if sorted(p) == p:
    print(0)
    exit()
ans = 0
stack = []

for i in range(n):
    if p[i] % 2 == i % 2:
        tf_list.append(False)
    else:
        tf_list.append(True)

tf_idx = 0
while(tf_idx < n - 1):
    add_idx = 0
    cur_idx = tf_idx
    if not tf_list[cur_idx]:
        while(True):
            if tf_list[cur_idx] == tf_list[cur_idx + 1]:
                stack.append('A {}'.format(cur_idx + 1))
                tf_list[cur_idx] = True
                tf_list[cur_idx + 1] = True
                p[cur_idx], p[cur_idx + 1] = p[cur_idx + 1], p[cur_idx]
                ans += 1
                break
            else:
                stack.append('B {}'.format(cur_idx + 1))
                p[cur_idx], p[cur_idx + 2] = p[cur_idx + 2], p[cur_idx]
                tf_list[cur_idx], tf_list[cur_idx + 2] = tf_list[cur_idx + 2], tf_list[cur_idx]
                cur_idx += 2
                ans += 1
    if tf_list[tf_idx]:
        tf_idx += 1

want = 1
while(want < n):
    idx = p.index(want)
    if idx + 1 != want:
        for i in range((idx - want + 1) // 2):
            stack.append('B {}'.format((idx + 1) - (i + 1) * 2))
            p[idx - i * 2], p[idx - (i + 1) * 2] = p[idx - (i + 1) * 2], p[idx - i * 2]
            ans += 1
    want += 1

print(ans)
for item in stack:
    print(item)