from itertools import permutations
def list2string(l):
    return "".join(l)

def check_initial_zero(s):
    flg = False
    if s[0] == 0:
        flg = True
    return flg

n = input()
ans = 0
for i in range(1 << len(n)):
    left = []
    right = []
    for j in range(len(n)):
        if i >> j & 1:
            left.append(n[j])
        else:
            right.append(n[j])
    if len(left) == 0 or len(right) == 0:
        continue
    
    for order_left in permutations(left):
        for order_right in permutations(right):
            left_num_str = list2string(order_left)
            if check_initial_zero(left_num_str):
                continue
            
            right_num_str = list2string(order_right)
            if check_initial_zero(right_num_str):
                continue

            ans = max(ans, (int(left_num_str) * int(right_num_str)))

print(ans)