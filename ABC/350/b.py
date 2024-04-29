n, q = map(int, input().split())
t = list(map(int, input().split()))

tooth = [True for _ in range(n)]

for i in t:
    i -= 1
    tooth[i] = not tooth[i]

print(sum(tooth))