s = input()
if int(s[0]) == 1:
    print("No")
    exit()

col = {7:0, 4:1, 8:2, 2:2, 5:3, 1:3, 9:4, 3:4, 6:5, 10:6}
pins = [[] for _ in range(7)]

for i, item in enumerate(s):
    c = col[i + 1]
    if int(item) == 1:
        pins[c].append(i + 1)

pin_exist_flg = None

for i, items in enumerate(pins):
    if pin_exist_flg is not None and not pin_exist_flg and len(items) > 0:
        print("Yes")
        exit()
    if len(items) > 0 and i != 6:
        pin_exist_flg = True
    if pin_exist_flg and len(items) == 0:
        pin_exist_flg = False

print("No")