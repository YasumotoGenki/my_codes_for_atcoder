s = []
for i in range(8):
    s.append(input())

for i in range(8):
    for j in range(8):
        if s[i][j] == "*":
            ans = chr(ord('a') + j) + str(8 - i)
            print(ans)
            exit()