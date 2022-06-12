q = int(input())

idx = 0
s = [] # [[number of balls, how many balls still in]]

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        s.append([query[1], query[2]])
    else:
        c = query[1]
        ans = 0
        while(c):
            if s[idx][1] > c:
                ans += c * s[idx][0]
                s[idx][1] -= c
                c = 0
            else:
                ans += s[idx][1] * s[idx][0]
                c -= s[idx][1]
                s[idx][1] = 0
                idx += 1
                
        print(ans)