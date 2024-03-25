ans = []
while(True):
    a = int(input())
    ans.append(a)
    if a == 0:
        break

for item in reversed(ans):
    print(item)