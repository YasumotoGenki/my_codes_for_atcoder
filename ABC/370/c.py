s = list(input())
t = list(input())

ans = []

while(s != t):
    smaller_idx = -1
    diff_idx = -1
    for i in range(len(t)):
        if s[i] != t[i]:
            diff_idx = i
            if s[i] > t[i]:
                smaller_idx = i
                break
        

    if smaller_idx != -1:
        s[smaller_idx] = t[smaller_idx]
    elif diff_idx != -1:
        s[diff_idx] = t[diff_idx]
    ans.append(s[:])

print(len(ans))
for i in range(len(ans)):
    print("".join(ans[i]))