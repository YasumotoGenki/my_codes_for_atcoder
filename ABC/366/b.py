n = int(input())
s = []
m = 0
for _ in range(n):
    text = input()
    m = max(m, len(text))
    s.append(text)

ans = [[] for _ in range(m)]

for char_idx in range(m):
    for idx_s in range(n):
        if len(s[idx_s]) <= char_idx:
            # if ans[char_idx] and ans[char_idx][-1] == "*":
            #     pass
            # else:
            ans[char_idx].append("*")
        else:
            ans[char_idx].append(s[idx_s][char_idx])

for i in range(m):
    output = ans[i][::-1]
    while(output[-1] == "*"):
        output.pop()
    print("".join(output))
