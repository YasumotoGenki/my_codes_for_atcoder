from collections import deque

n = int(input())
a = list(map(int, input().split()))

duplicated = []
a_set = set()
for item_a in a:
    if item_a not in a_set:
        a_set.add(item_a)
    else:
        duplicated.append(item_a)
a = list(a_set)
a.sort()
deque_a = deque(a)
current_id = 0
stack = []

while(True):
    if deque_a:
        book_id = deque_a.popleft()
        if book_id == current_id + 1:
            stack.append(book_id)
            current_id += 1
            continue
        deque_a.appendleft(book_id)
    sell_num = 0
    while(sell_num < 2):
        if duplicated:
            duplicated.pop()
            sell_num += 1
        elif deque_a:
            deque_a.pop()
            sell_num += 1
        else:
            break
    if sell_num == 2:
        stack.append(current_id + 1)
        current_id += 1
    else:
        break
print(len(stack))