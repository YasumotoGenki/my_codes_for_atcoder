from collections import Counter

s = input()
counter = Counter(s)

value_counter = dict()
for key, value in counter.items():
    if value not in value_counter:
        value_counter[value] = 1
    else:
        value_counter[value] += 1

for value, count in value_counter.items():
    if count == 0 or count == 2:
        pass
    else:
        print("No")
        exit()

print("Yes")