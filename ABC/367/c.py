n, k = map(int, input().split())
r = list(map(int, input().split()))

def dfs(stack_list):
    current_len = len(stack_list)
    if current_len == n:
        if sum(stack_list) % k == 0:
            ans = [str(item) for item in stack_list]
            print(" ".join(ans))
    else:
        for i in range(1, r[current_len] + 1):
            dfs(stack_list + [i])
dfs([])