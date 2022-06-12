from bisect import bisect_left, bisect_right
n = int(input())
a = list(map(int, input().split()))
q = int(input())
element_to_indices_dict = dict()
for i in range(n):
    if a[i] not in element_to_indices_dict:
        element_to_indices_dict[a[i]] = [i]
    else:
        element_to_indices_dict[a[i]].append(i)

for i in range(q):
    l, r, x = map(int, input().split())
    l -= 1
    r -= 1
    if x in element_to_indices_dict:
        left_index = bisect_left(element_to_indices_dict[x], l)
        right_index = bisect_right(element_to_indices_dict[x], r)
        print(right_index - left_index)
    else:
        print(0)