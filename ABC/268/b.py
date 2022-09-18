s = input()
t = input()

if len(s) > len(t):
    print("No")
    exit()

l = len(s)
if s == t[:l]:
    print("Yes")
else:
    print("No")