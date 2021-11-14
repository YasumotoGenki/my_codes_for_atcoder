s = input()
idx = s.find('.') + 1
if int(s[idx]) >= 5:
    print(int(float(s)) + 1)
else:
    print(int(float(s)))