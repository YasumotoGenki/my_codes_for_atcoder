n = int(input())
st = []
for i in range(n):
    cur_s, cur_t = map(str, input().split())
    st.append(cur_s)
    st.append(cur_t)

for i in range(n):
    if st.count(st[2 * i]) == 1 or st.count(st[2 * i + 1]) == 1 or (st.count(st[2 * i]) == 2 and st[2 * i] == st[2 * i + 1]):
        pass
    else:
        print("No")
        exit()
print("Yes")
