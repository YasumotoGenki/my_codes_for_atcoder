n, w = map(int, input().split())
a = list(map(int, input().split()))

ans = set()
for i, item_1 in enumerate(a):
    for j, item_2 in enumerate(a):
        for k, item_3 in enumerate(a):
            if item_1 <= w:
                ans.add(item_1)
            if i != j and item_1 + item_2 <= w:
                ans.add(item_1 + item_2)
            if i != j and j != k and k != i and item_1 + item_2 + item_3 <= w:
                ans.add(item_1 + item_2 + item_3)
print(len(ans))
