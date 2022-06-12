n = int(input())
t = list(map(int, input().split()))
ans = []

for i in range(n):
    if i == 0:
        ans.append(int('1' + '0' * t[i], 2))
    else:
        if ans[-1] < int('1' + '0' * t[i], 2):
            ans.append(int('1' + '0' * t[i], 2))
            continue
        
        else:
            cur_ans = ((ans[-1] >> t[i]) + 1) | 1
            cur_ans = cur_ans << t[i]
            ans.append(cur_ans)

print(ans[-1])