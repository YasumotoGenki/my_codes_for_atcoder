n = int(input())

for i in range(n, 920):
    string_num = str(i)
    if int(string_num[0]) * int(string_num[1]) == int(string_num[2]):
        print(i)
        exit()