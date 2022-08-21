r, c = map(int, input().split())
ans = "white"
if r == 1 or r == 15 or c == 1 or c == 15:
    ans = "black"
elif (r == 3 or r == 13) and 3 <= c <= 13:
    ans = "black"
elif (c == 3 or c == 13) and 3 <= r <= 13:
    ans = "black"
elif (r == 5 or r == 11) and 5 <= c <= 11:
    ans = "black"
elif (c == 5 or c == 11) and 5 <= r <= 11:
    ans = "black"
elif (r == 7 or r == 9) and 7 <= c <= 9:
    ans = "black"
elif (c == 7 or c == 9) and 7 <= r <= 9:
    ans = "black"
print(ans)