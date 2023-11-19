b = int(input())

a = 1
while(a ** a <= b):
    if a ** a == b:
        print(a)
        exit()
    else:
        a += 1

print(-1)