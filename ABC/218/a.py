x = int(input())

if x >= 90:
    ans = "expert"
elif x >= 70:
    ans = 90 - x
elif x >= 40:
    ans = 70 - x
else:
    ans = 40 - x

print(ans)

