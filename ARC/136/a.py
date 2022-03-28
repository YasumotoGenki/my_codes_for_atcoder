n = int(input())
s = input()

a_count = 0
b_bount = 0
ans = []

for i in range(n):
    if s[i] == "C":
        a_count += b_bount // 2
        b_bount = b_bount % 2
        for j in range(a_count):
            ans.append("A")
        if b_bount:
            ans.append("B")
        a_count = 0
        b_bount = 0
        ans.append("C")
    else:
        if s[i] == "A":
            a_count += 1
        else:
            b_bount += 1

a_count += b_bount // 2
b_bount = b_bount % 2
for j in range(a_count):
    ans.append("A")
if b_bount:
    ans.append("B")

print("".join(ans))