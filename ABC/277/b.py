n = int(input())
ans = True
s_set = set()
for i in range(n):
    s = input()
    if s[0] not in ["H", "D", "C", "S"]:
        ans = False
    if s[1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
        ans = False
    if s in s_set:
        ans = False
    s_set.add(s)
if ans:
    print("Yes")
else:
    print("No")