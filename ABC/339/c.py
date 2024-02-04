n = int(input())
a = list(map(int, input().split()))

stack = 0
min_value = 10 ** 10
for item_a in a:
    stack += item_a
    if min_value > stack:
        min_value = stack

if min_value >= 0:
    print(stack)
else:
    print(-min_value + stack)