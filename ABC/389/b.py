x = int(input())

c = 1
for i in range(1, 100):
    c *= i
    if x == c:
        print(i)