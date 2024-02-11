q = int(input())
stack = []
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        stack.append(query[1])
    else:
        print(stack[-query[1]])