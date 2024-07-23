from itertools import permutations

n, k = map(int, input().split())
s = input()

count = 0
appeared_set = set()
for candidate in permutations(s, n):
    candidate = "".join(candidate)
    if candidate in appeared_set:
        continue
    appeared_set.add(candidate)
    # check kaibun
    for i in range(n - k + 1):
        flg = True
        for j in range(k // 2):
            if candidate[i + j] != candidate[i + k - 1 - j]:
                flg = False
                break
        if flg:
            break
    if not flg:
        count += 1

print(count)