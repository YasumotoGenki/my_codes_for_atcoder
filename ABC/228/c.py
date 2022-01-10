n, k = map(int, input().split())

total_list = []

for i in range(n):
    total_list.append(sum(list(map(int, input().split()))))

sorted_total = sorted(total_list, reverse=True)

for i in range(n):
    c_total =  total_list[i]
    k_total = sorted_total[k - 1]
    if c_total + 300 >= k_total:
        print("Yes")
    else:
        print("No")