n = int(input())

s = ""

while(n > 0):
    if n > 0 and n % 2 == 0:
        n //= 2
        s += "B"
    else:
        n -= 1
        s += "A"
    
ans = s[::-1]
print(ans)