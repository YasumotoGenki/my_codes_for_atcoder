s = input()
stack = []

for character in s:
    stack.append(character)
    if len(stack) >= 3:
        if "".join(stack[-3:]) == "ABC":
            for i in range(3):
                stack.pop()

print("".join(stack))