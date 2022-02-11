n, m = map(int, input().split())
s = list(map(str, input().split()))
t = list(map(str, input().split()))

set_t = set(t)

for station in s:
    if station in set_t:
        print("Yes")
    else:
        print("No")

