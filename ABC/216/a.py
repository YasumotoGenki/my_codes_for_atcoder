x, y = map(int, input().split("."))

if y <= 2:
    print("{0}-".format(x))
elif y <= 6:
    print("{0}".format(x))
else:
    print(("{0}+".format(x)))