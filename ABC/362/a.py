r, g, b = map(int, input().split())
c = input()

if c == 'Red':
    ans = min(g, b)
elif c == 'Green':
    ans = min(r, b)
else:
    ans = min(r, g)

print(ans)