n = int(input())
s = input()

abc_set = set()
for i in range(n):
    abc_set.add(s[i])
    if len(abc_set) == 3:
        print(i + 1)
        exit()
