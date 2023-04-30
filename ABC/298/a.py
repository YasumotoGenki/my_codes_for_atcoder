n = int(input())
s = input()

good_flg = False

for i in range(n):
    if s[i] == 'x':
        print("No")
        exit()
    if s[i] == "o":
        good_flg = True
if good_flg:
    print("Yes")
else:
    print("No")