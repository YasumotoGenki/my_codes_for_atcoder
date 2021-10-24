h, w = map(int, input().split())
list_a = []
for i in range(h):
    list_a.append(list(map(int, input().split())))

for h_i in range(h - 1):
    for w_i in range(w - 1):
        if list_a[h_i][w_i] + list_a[h_i + 1][w_i + 1] > list_a[h_i + 1][w_i] + list_a[h_i][w_i + 1]:
            print("No")
            exit()
else:
    print("Yes")