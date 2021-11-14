possible_s_set = set()
for a in range(1, 142):
    for b in range(1, 142):
        s = 4 * a * b + 3 * a + 3 * b
        if s <= 1000:
            possible_s_set.add(s)

n = int(input())
s_input_list = list(map(int, input().split()))

ans = 0
for i in range(n):
    if s_input_list[i] not in possible_s_set:
        ans += 1
print(ans)