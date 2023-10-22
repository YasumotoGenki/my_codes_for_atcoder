import heapq

n, a, b, c = map(int, input().split())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))

cost_and_node_heap_list = [[0, 0]]
heapq.heapify(cost_and_node_heap_list)
node2cost_dict = [10 ** 50 for _ in range(n)]
node2cost_dict[0] = 0

while(cost_and_node_heap_list):
    current_cost, current_node = heapq.heappop(cost_and_node_heap_list)
    if node2cost_dict[current_node] != current_cost:
        continue
    for next_node, element_d in enumerate(d[current_node]):
        if current_cost + a * element_d < node2cost_dict[next_node]:
            node2cost_dict[next_node] = current_cost + a * element_d
            heapq.heappush(cost_and_node_heap_list, [current_cost + a * element_d, next_node])

for i in range(n):
    cost_and_node_heap_list.append([node2cost_dict[i], i])
while(cost_and_node_heap_list):
    current_cost, current_node = heapq.heappop(cost_and_node_heap_list)
    if node2cost_dict[current_node] != current_cost:
        continue
    for next_node, element_d in enumerate(d[current_node]):
        if current_cost + b * element_d + c < node2cost_dict[next_node]:
            node2cost_dict[next_node] = current_cost + b * element_d + c
            heapq.heappush(cost_and_node_heap_list, [current_cost + b * element_d + c, next_node])

print(node2cost_dict[n - 1])