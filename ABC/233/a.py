x, y = map(int, input().split())

ans = 0
while(True):
    if ans * 10 + x >= y:
        print(ans)
        exit()
    else:
        ans += 1