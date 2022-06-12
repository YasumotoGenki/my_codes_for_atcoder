n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_value = max(a)
indices = [i + 1 for i, item in enumerate(a) if item == max_value]

for idx in indices:
    if idx in b:
        print("Yes")
        exit()
print("No")