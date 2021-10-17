s = input()

ans_list = []
for i in range(len(s)):
    ans_list.append(s[i:] + s[:i])
ans_list = sorted(ans_list)
print(ans_list[0])
print(ans_list[-1])
