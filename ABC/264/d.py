s = input()

int_s = []
d = {'a': 0, 't': 1, 'c': 2, 'o': 3, 'd': 4, 'e': 5, 'r': 6}

for i in s:
    int_s.append(d[i])

ans = 0
for i in range(7):
    for j in range(i + 1, 7):
        if int_s[i] > int_s[j]:
            ans += 1
print(ans)