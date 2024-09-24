n, q = map(int, input().split())
s = input()
s_list= list(s)

ans = 0

for i in range(len(s) - 2):
    if s[i:i+3] == "ABC":
        ans += 1

for _ in range(q):
    x, c = map(str, input().split())
    x = int(x) - 1

    for start_idx in range(-2, 1):
        if x + start_idx < 0:
            continue
        if x + start_idx + 2 > len(s) - 1:
            continue
        if "".join(s_list[x + start_idx: x + start_idx + 3]) == "ABC":
            ans -= 1
        replaced_char = s_list[x + start_idx: x + start_idx + 3]
        replaced_char[-start_idx] = c
        if "".join(replaced_char) == "ABC":
            ans += 1
    s_list[x] = c
    print(ans)