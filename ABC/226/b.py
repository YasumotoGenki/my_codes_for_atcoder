n = int(input())
set_a = set()
for i in range(n):
    input_tuple = tuple(map(int, input().split()))
    set_a.add(input_tuple)
print(len(set_a))