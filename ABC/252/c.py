n = int(input())
s = []
for i in range(n):
    s.append(input())

ans = 10 ** 10

for i in range(10):
    count = [0 for _ in range(10)]
    i = str(i)
    for item_s in s:    
        idx = item_s.index(i)
        count[idx] += 1
    ans = min(ans, 10 * max(count) - count[-1::-1].index(max(count)) - 1)
print(ans)
