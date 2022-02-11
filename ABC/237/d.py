n = int(input())
s = input()

pointer = 0
rev_pointer = n
ans = [None] * (n + 1)
pending_str = "0"

for i in range(n):
    if s[i] == "R":
        ans[pointer] = pending_str
        pointer += 1
        pending_str = str(i + 1)
    else:
        ans[rev_pointer] = pending_str
        rev_pointer -= 1
        pending_str = str(i + 1)
ans[pointer] = pending_str

print(*ans)