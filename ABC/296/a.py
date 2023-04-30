n = int(input())
s = input()

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        pass
    else:
        print("No")
        exit()
print("Yes")