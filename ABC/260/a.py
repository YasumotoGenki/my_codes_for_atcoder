s = input()
count = dict()
for item in s:
    if item not in count:
        count[item] = 1
    else:
        count[item] += 1

for key, value in count.items():
    if value == 1:
        print(key)
        exit()
print(-1)