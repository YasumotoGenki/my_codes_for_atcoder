n = int(input())
s = input()

for i in range(1, n):
    if s[i] == "a" and s[i - 1] == "b" or s[i] == "b" and s[i - 1] ==  "a":
        print("Yes")
        exit()
print("No")