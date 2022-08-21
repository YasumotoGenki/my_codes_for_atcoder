y = int(input())
rem = y % 4
if rem == 2:
    print(y)
elif rem > 2:
    print(y + rem)
else:
    print(y + 2 - rem)