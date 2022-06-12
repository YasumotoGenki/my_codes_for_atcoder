from itertools import combinations


n, k = map(int, input().split())
s_list = []
for i in range(n):
    s_list.append(input())

ans = 0

for j in range(1, n + 1):
    for cmbs in combinations(s_list, j):
        chr_count_list = [0 for _ in range(26)]
        for i in range(26):    
            character = chr(ord('a') + i)
            for cur_s in cmbs:
                if character in cur_s:
                    chr_count_list[i] += 1
        tentative_ans = 0
        for i in range(26):
            if chr_count_list[i] == k:
                tentative_ans += 1
        if tentative_ans > ans:
            ans = tentative_ans

print(ans)