m = int(input())

ans = []
while(m > 0):
    i = 0
    while(3 ** (i + 1) <= m and i < 10):
        i += 1
    m -= 3 ** i
    ans.append(str(i))

print(len(ans))
print(" ".join(ans))