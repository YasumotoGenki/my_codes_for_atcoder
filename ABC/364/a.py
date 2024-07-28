n = int(input())
prev = ""
for i in range(n - 1):
    s = input()
    if s == prev == "sweet":
        print("No")
        exit()
    prev = s

print("Yes")