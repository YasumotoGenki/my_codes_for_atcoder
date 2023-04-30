n = int(input())

left = 1
right = n

idx_to_num_dict = dict()
idx_to_num_dict[1] = 0
idx_to_num_dict[n] = 1

if n == 2:
    print("! 1")
    exit()

for _ in range(20):
    middle = (right + left) // 2
    print("? {}".format(middle))
    s_i = int(input())
    if s_i == 0:
        idx_to_num_dict[middle] = 0
        left = middle
    else:
        idx_to_num_dict[middle] = 1
        right = middle
    if right - left <= 1:
        break
if left in idx_to_num_dict and left + 1 in idx_to_num_dict \
    and idx_to_num_dict[left] != idx_to_num_dict[left + 1]:
    print("! {}".format(left))
    exit()

if right in idx_to_num_dict and right + 1 in idx_to_num_dict \
    and idx_to_num_dict[right] != idx_to_num_dict[right + 1]:
    print("! {}".format(right))
    exit()
