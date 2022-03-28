n = int(input())
a = list(map(int, input().split()))
set_a = set(a)

for i in range(2002):
    if i not in set_a:
        print(i)
        exit()