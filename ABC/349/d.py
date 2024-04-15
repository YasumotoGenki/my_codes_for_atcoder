l, r = map(int,  input().split())

def factrization_by_two(num):
    count = 0
    temp = num
    while(temp % 2 == 0):
        count += 1
        temp //= 2
    return count


ans = []
while(l < r):
    if l == 0:
        temp = r
        count = 0
        while(temp > 0):
            temp //= 2
            count += 1
    else:
        count = factrization_by_two(l)
    if count == 0:
        ans.append([l, l + 1])
        l += 1
    else:
        for i in range(count, -1, -1):
            base = (2 ** i)
            rem = l // base
            if r >= base * (rem + 1):
                ans.append([l, base * (rem + 1)])
                l = base * (rem + 1)
                break
print(len(ans))
for i in range(len(ans)):
    print(ans[i][0], ans[i][1])
