
from math import log2
from itertools import combinations

n = int(input())
all_edge_cost = [dict() for _ in range(n)]
for i in range(n - 1):
    node_i_edge_list = list(map(int, input().split()))
    for j, cost in enumerate(node_i_edge_list):
        all_edge_cost[i][i+ j + 1] = cost

dp = [[None for _ in range(2 ** n)] for _ in range(n // 2 + 1)]
dp[0][0] = 0

ans = 0
binary_node_list = [2 ** i for i in range(n)]
for dege_num in range(n // 2):
    # 現在の選択されたノード
    for binary_selected_node in range(2 ** n):
        if dp[dege_num][binary_selected_node] is None:
            continue
        # どの辺を選ぶかを２進数で考える
        for a, b in combinations(binary_node_list, 2):
            if binary_selected_node & a == 0 and binary_selected_node & b == 0:
                next_binary_selected_node = binary_selected_node | a | b
                a, b = int(log2(a)), int(log2(b))
                if dp[dege_num + 1][next_binary_selected_node] is None:
                    dp[dege_num + 1][next_binary_selected_node] = all_edge_cost[a][b]
                else:
                    dp[dege_num + 1][next_binary_selected_node] = max(dp[dege_num + 1][next_binary_selected_node], dp[dege_num][binary_selected_node] + all_edge_cost[a][b])
                
                if ans < dp[dege_num + 1][next_binary_selected_node]:
                        ans = dp[dege_num + 1][next_binary_selected_node]

print(ans)