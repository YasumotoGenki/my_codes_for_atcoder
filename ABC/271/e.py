n, m, k = map(int, input().split())
road = []
start_point_indices = []
for i in range(m):
    a, b, c = map(int, input().split())
    road.append([a, b, c])
    if a == 1:
        start_point_indices.append(i)

if len(start_point_indices) == 0:
    print(-1)
    exit()

e = list(map(int, input().split()))

cost_list = [None] * n
cost_list[0] = 0

for road_i in e:
    road_i -= 1
    cur_node = road[road_i][0] - 1
    if cost_list[cur_node] != None:
        next_node = road[road_i][1] - 1
        cur_cost = road[road_i][2]
        if cost_list[next_node] != None:
            cost_list[next_node] = min(cost_list[next_node], cost_list[cur_node] + cur_cost)
        else:
            cost_list[next_node] = cost_list[cur_node] + cur_cost
if cost_list[-1] != None:
    print(cost_list[-1])
else:
    print(-1)
