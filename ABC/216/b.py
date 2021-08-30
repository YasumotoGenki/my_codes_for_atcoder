n = int(input())
names = []
for i in range(n):
    s, t = map(str, input().split())
    names.append("{0} {1}".format(s, t))

for i in range(n):
    for j in range(i + 1, n):
        if names[i] == names[j]:
            print("Yes")
            exit()
print("No")
