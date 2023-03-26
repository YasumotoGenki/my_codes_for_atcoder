n = int(input())
w = list(map(str, input().split()))

for item in w:
    if item == "and" or item == "not" or item == "that" or item == "the" or item == "you":
        print("Yes")
        exit()
else:
    print("No")