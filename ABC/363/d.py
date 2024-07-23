n = int(input())

k = 0
digit = 0
while(k < n):
    digit += 1
    if k == 0:
        k += 10
    else:
        k += 9 * (10 ** ((digit - 1) // 2))

if digit == 1:
    print(n - 1)
    exit()

k -= 9 * (10 ** ((digit - 1) // 2))

ans = ["0" for _ in range(digit)]

for i in range((digit // 2) + (digit % 2)):
    for j in range(10):
        if j == 0 and i == 0:
            continue
        if k + 10 ** ((digit // 2) + (digit % 2) - 1 - i) < n:
            k += 10 ** ((digit // 2) + (digit % 2) - 1 - i)
        else:
            ans[i] = str(j)
            ans[-1 - i]  = str(j)
            break

print("".join(ans))