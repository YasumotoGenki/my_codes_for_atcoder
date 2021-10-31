s = input()
kinds = len(set(s))
if kinds == 3:
    print(6)
elif kinds == 2:
    print(3)
else:
    print(1)