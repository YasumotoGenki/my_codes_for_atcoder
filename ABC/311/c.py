import sys
sys.setrecursionlimit(1000000)

n = int(input())
a = list(map(int, input().split()))

def dfs(current_node: int, visited_set: set, visited_list: list):
    global a
    current_node -=1
    next_node = a[current_node]
    current_node += 1
    if next_node in visited_set:
        idx = visited_list.index(next_node)
        visited_list.append(current_node)
        visited_set.add(current_node)
        # print(*visited_list[idx:])
        return visited_list[idx:]
    else:
        visited_set.add(current_node)
        visited_list.append(current_node)
        return dfs(next_node, visited_set, visited_list)

ans_nodes = dfs(1, set(), [])

print(len(ans_nodes))
print(*ans_nodes)