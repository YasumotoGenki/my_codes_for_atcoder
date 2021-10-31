n = int(input())

for i in range(n - 1):
    a, b = map(int, input().split())
    if i == 0:
        candidate = [a, b]
    else:
        remove_list = []
        for cidx, c in enumerate(candidate):
            if c not in [a, b]:
                remove_list.append(cidx)
        for cidx in sorted(remove_list, reverse=True):
            candidate.pop(cidx)
        if len(candidate) == 0:
            print("No")
            exit()
print("Yes")
