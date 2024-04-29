n = int(input())
a = list(map(int, input().split()))

stack = []

for item in a:
    stack.append(item)
    while(len(stack) > 1 and stack[-1] == stack[-2]):
        stack.pop()
        stack[-1] += 1
print(len(stack))