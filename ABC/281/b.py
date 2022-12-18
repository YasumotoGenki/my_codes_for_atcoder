nums = [str(i) for i in range(10)]

s = input()
if len(s) != 8:
    print("No")
    exit()
if s[0] in nums or s[-1] in nums:
    print("No")
    exit()
for i in range(1, 7):
    if s[i] not in nums:
        print("No")
        exit()
if int(s[1:7]) < 100000 or int(s[1:7]) > 1000000:
    print("No")
    exit()
print("Yes")