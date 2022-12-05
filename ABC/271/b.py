n, q = map(int, input().split())
l_list = []
a_list = []
for i in range(n):
    input_list = list(map(int, input().split()))
    l_list.append(input_list[0])
    a_list.append(input_list[1:])
for i in range(q):
    s, t = map(int, input().split())
    print(a_list[s - 1][t - 1])