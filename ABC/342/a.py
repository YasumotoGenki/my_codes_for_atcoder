from collections import Counter
s = input()
counter = Counter(s)
for k, v in counter.items():
    if v == 1:
        idx = s.index(k)
        print(idx + 1)
        exit()