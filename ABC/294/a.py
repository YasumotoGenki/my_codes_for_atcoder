n = int(input())
a = list(map(int, input().split()))

ans_list = []

for item_a in a:
    if item_a % 2 == 0:
        ans_list.append(item_a)

print(*ans_list)