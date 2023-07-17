n = int(input())

string_set = set()

for i in range(n):
    s = input()
    string_set.add(s)
    string_set.add(s[::-1])

count = len(string_set)

for item in string_set:
    if item == item[::-1]:
        count += 1

ans = count // 2
print(ans)