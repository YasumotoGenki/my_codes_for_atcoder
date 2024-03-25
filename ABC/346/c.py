n, k = map(int, input().split())
a = list(map(int, input().split()))

summation = k * (2 + k - 1) // 2

done = set()
for item_a in a:
    if item_a not in done and item_a <= k:
        summation -= item_a
        done.add(item_a)
print(summation)