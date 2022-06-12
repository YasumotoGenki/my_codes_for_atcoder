a, b, c, d, e, f, x = map(int, input().split())
ac = a + c
df = d + f
takahashi_walk_time = (x // ac) * a + min(a, x % ac)
aoki_walk_time = (x // df) * d + min(d, x % df)
if takahashi_walk_time * b == aoki_walk_time * e:
    print("Draw")
elif takahashi_walk_time * b > aoki_walk_time * e:
    print("Takahashi")
else:
    print("Aoki")