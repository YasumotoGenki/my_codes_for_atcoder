from collections import Counter


n = int(input())
a = list(map(int, input().split()))
a_elements_counter = Counter(a)
ans = 0

for key, value in a_elements_counter.items():
    ans += (value // 2)

print(ans)