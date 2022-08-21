cards = list(map(int, input().split()))
kinds = len(set(cards))

if kinds != 2:
    print("No")
    exit()

for item in cards:
    if cards.count(item) == 2 or cards.count(item) == 3:
        print("Yes")
        exit()
    else:
        print("No")
        exit()