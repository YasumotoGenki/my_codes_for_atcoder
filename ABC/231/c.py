N, Q = map(int, input().split())
A = list(map(int, input().split()))

query_list = []
for i in range(Q):
    x = int(input())
    query_list.append(x)

sorted_A = sorted(A, reverse=True)
sorted_query_list = sorted(query_list, reverse=True)

q_idx = 0
a_idx = 0
ans_dict = dict()
while(q_idx < Q):
    x = sorted_query_list[q_idx]
    while(a_idx < N and sorted_A[a_idx] >= x):
        a_idx += 1
    ans_dict[x] = a_idx
    q_idx += 1

for i in range(Q):
    x = query_list[i]
    print(ans_dict[x])