import sys
sys.setrecursionlimit(100000)

n = int(input())
road_list = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    road_list[a].append(b)
    road_list[b].append(a)

distance = []
goal = []
def dfs(cur_idx, next_idx, dist):
    distance.append(dist)
    goal.append(next_idx)
    for road in road_list[next_idx]:
        if road != cur_idx:
            dfs(next_idx, road, dist + 1)


for road in road_list[0]:
    dfs(0, road, 1)
far = max(distance)
far_idx = distance.index(far)
distance = []
start = goal[far_idx]
goal = []
for road in road_list[start]:
    dfs(start, road, 1)

far = max(distance)

print(far + 1)