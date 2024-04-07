n = int(input())
ac = dict()
for _ in range(n):
    a, c = map(int, input().split())
    if c not in ac:
        ac[c] = a
    ac[c] = min(ac[c], a)

max_value = 0
for c, a in ac.items():
    if a > max_value:
        max_value = a
print(max_value)
