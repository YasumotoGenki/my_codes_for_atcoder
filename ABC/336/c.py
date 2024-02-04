n = int(input())
digit = 1
count = 5
while(count < n):    
    digit += 1
    count += 4 * (5 ** (digit - 1))

if digit == 1:
    ans = n * 2 - 2
else:
    ans = 0
    while(digit > 1):
        for i in range(5):
            n -= 5 ** (digit - 1)
            if n <= 0:
                ans += i * 2 * (10 ** (digit - 1))
                n += 5 ** (digit - 1)
                break

        digit -= 1
    ans += n * 2 - 2
        
print(ans)