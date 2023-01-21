n = int(input())
st = dict()

for i in range(n):
    s, t = map(str, input().split())
    st[s] = t

done = set()
for s, t in st.items():
    cur_s, cur_t = s, t
    if cur_s in done:
        continue
    done.add(s)
    visited = set()
    visited.add(s)
    while(cur_t in st):
        done.add(cur_t)
        cur_s = cur_t
        cur_t = st[cur_t]
        if cur_t in visited:
            print("No")
            exit()
        else:
            visited.add(cur_s)
print("Yes")
