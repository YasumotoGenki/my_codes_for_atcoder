from itertools import permutations

n = int(input())
a = list(map(str, input().split()))

digit_list = [[] for _ in range(6)]

for item_a in a:
    digit_list[len(item_a) - 1].append(item_a)

stack = []
count = 0
for i in range(5, -1, -1):
    digit_list[i].sort(reverse=True)
    for item in digit_list[i]:
        stack.append(item)
        count += 1
        if count >= 3:
            break
    if count >= 3:
        break

ans = 0
for items in permutations(stack):
    cur = int(items[0] + items[1] + items[2])
    ans = max(ans, cur)
print(ans)