from collections import Counter

n = int(input())
s = input()

counter_s = Counter(s)
max_s = int("".join(sorted(list(s), reverse=True)))

i = 0
limit = 10 ** n
ans = 0
while (i ** 2 <= max_s):
    flg = True
    if len(str(i ** 2)) < n:
        num_zeros = n - len(str(i ** 2))
        candidate = '0' * num_zeros + str(i ** 2)
        counter_candidate = Counter(candidate)
    else:
        counter_candidate = Counter(str(i ** 2))
    for key, value in counter_s.items():
        if key in counter_candidate and counter_candidate[key] == value:
            pass
        else:
            flg = False
            break
    for key, value in counter_candidate.items():
        if key in counter_s and counter_s[key] == value:
            pass
        else:
            flg = False
            break
    if flg:
        ans += 1
    i += 1
print(ans)
