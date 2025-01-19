q = int(input())
s = [0]
idx = 0
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        s.append(s[-1] + query[1])
    elif query[0] == 2:
        idx += 1
    else:
        print(s[idx + query[1] - 1] - s[idx])