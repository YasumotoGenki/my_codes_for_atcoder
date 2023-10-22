n = int(input())
time_to_people = dict()
for i in range(24):
    time_to_people[i] = 0
for i in range(n):
    w, x = map(int, input().split())
    for j in range(9):
        time = (x + j) % 24
        time_to_people[time] += w
print(max(time_to_people.values()))