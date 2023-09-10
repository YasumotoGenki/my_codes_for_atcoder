n, m = map(int, input().split())
l = list(map(int, input().split()))

large = 2 * (10 ** 15)
small = max(l)

while(large - small > 1):
    middle = (large + small) // 2
    count = 0
    l_idx = 0
    m_idx = 1
    while(l_idx < n):
        if count + l[l_idx] <= middle:
            count += l[l_idx]
        else:
            count = l[l_idx]
            m_idx += 1
        l_idx += 1
        count += 1
    if m_idx <= m:
        large = middle
    else:
        small = middle

count = 0
l_idx = 0
m_idx = 1
while(l_idx < n):
    if count + l[l_idx] <= small:
        count += l[l_idx]
    else:
        count = l[l_idx]
        m_idx += 1
    l_idx += 1
    count += 1
if m_idx <= m:
    print(small)
else:
    print(large)