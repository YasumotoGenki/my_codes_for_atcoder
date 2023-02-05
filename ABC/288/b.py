n, k = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

high_rank = s[:k]
high_rank.sort()
for i in range(k):
    print(high_rank[i])