s = input()
for i in range(1, 16, 2):
    if s[i] == "0":
        pass
    else:
        print("No")
        exit()
print("Yes")