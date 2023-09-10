n = int(input())
candidate_j_list = []
for j in range(1, 10):
    if n % j == 0:
        candidate_j_list.append(j)

ans = []
for i in range(n + 1):
    for j in candidate_j_list:
        if i % (n // j) == 0:
            ans.append(str(j))
            break
    else:
        ans.append("-")
print("".join(ans))
