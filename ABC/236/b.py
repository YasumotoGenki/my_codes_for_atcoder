n = int(input())
a = list(map(int, input().split()))

count_list = [0] * n
for item in a:
    item -= 1
    count_list[item] += 1

for i, count in enumerate(count_list):
    if count == 3:
        print(i + 1)
        exit()