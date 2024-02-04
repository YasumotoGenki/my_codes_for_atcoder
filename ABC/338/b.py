from collections import Counter
s = input()
counter = Counter(s)
max_value = max(counter.values())
for k in sorted(counter.keys()):
    if counter[k] == max_value:
        print(k)
        exit()