n, m = map(int, input().split())
weak_2_strong_dict = dict()
strong_2_weak_dict = dict()

for i in range(m):
    a, b = map(int, input().split())
    if b in weak_2_strong_dict:
        weak_2_strong_dict[b] += [a]
    else:
        weak_2_strong_dict[b] = [a]
    if a in strong_2_weak_dict:
        strong_2_weak_dict[a] += [b]
    else:
        strong_2_weak_dict[a] = [b]

all_programmer_set = set([i for i in range(1, n + 1)])
weak_programmer_set = set([programmer for programmer in weak_2_strong_dict.keys()])

if len(all_programmer_set - weak_programmer_set) == 1:
    strongest_programmer = (all_programmer_set - weak_programmer_set).pop()
    print(strongest_programmer)
else:
    print(-1)
