n = int(input())

top = 1
bottom = n

# search h index where to place Luke
while(bottom - top > 1):
    # ask question
    middle = (top + bottom) // 2
    print("?", "{0} {1} {2} {3}".format(top, middle, 1, n), flush=True)
    ans = int(input())
    if middle - top + 1 == ans:
        top = middle + 1
    else:
        bottom = middle
print("?", "{0} {1} {2} {3}".format(top, top, 1, n), flush=True)
ans = int(input())
if ans == 0:
    h_idx = top
else:
    h_idx = top + 1
# search w index where to place Luke
left = 1
right = n
while(right - left > 1):
    # ask question
    middle = (left + right) // 2
    print("?", "{0} {1} {2} {3}".format(1, n, left, middle), flush=True)
    ans = int(input())
    if middle - left + 1 == ans:
        left = middle + 1
    else:
        right = middle
print("?", "{0} {1} {2} {3}".format(1, n, left, left), flush=True)
ans = int(input())
if ans == 0:
    w_idx = left
else:
    w_idx = left + 1
print("!", h_idx, w_idx)