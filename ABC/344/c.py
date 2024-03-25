n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
l = int(input())
c = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))

can_be_x = dict()

for item in x:
    if item not in can_be_x:
        can_be_x[item] = False

for item_a in a:
    for item_b in b:
        for item_c in c:
            value = item_a + item_b + item_c
            if value in can_be_x:
                can_be_x[value] = True

for item in x:
    if can_be_x[item]:
        print("Yes")
    else:
        print("No")