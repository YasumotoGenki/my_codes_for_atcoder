x = input()
count = 0
for i in range(1, len(x) + 1):
    if x[-i] == '0':
        count += 1
    elif x[-i] == '.':
        count += 1
        break
    else:
        break
if count == len(x):
    print(0)
elif count > 0:
    print(x[:-count])
else:
    print(x)