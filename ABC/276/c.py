from math import factorial

n = int(input())
p = list(map(int, input().split()))
num_list = [1 for _ in range(n)]


# seek current num order
count = 0
for i, item in enumerate(p):
    if item == 1:
        num_list[0] = 0
        continue
    smaller_num_sum = sum(num_list[:item - 1])
    count += smaller_num_sum * factorial(n - i - 1)
    num_list[item - 1] = 0

# seek previous num
ans = []
num_list = [1 for _ in range(n)]
stack = 0
for i in range(n):
    max_num = 0
    max_cur_stack = 0
    for j in range(n):
        if num_list[j]:
            smaller_num_sum = sum(num_list[:j])
            cur_stack = smaller_num_sum * factorial(n - i - 1)
            if stack + cur_stack < count:
                max_num = j + 1
                max_cur_stack = cur_stack
    ans.append(max_num)
    num_list[max_num - 1] = 0
    stack += max_cur_stack

print(*ans)