n = int(input())
s = input()
q = int(input())
transform_dict = dict()
for i in range(26):
    letter = chr(ord('a') + i)
    transform_dict[letter] = letter

for _ in range(q):
    c, d = map(str, input().split())
    for i in range(26):
        letter = chr(ord('a') + i)
        if transform_dict[letter] == c:
            transform_dict[letter] = d

ans = []
for i in range(n):
    ans.append(transform_dict[s[i]])

print("".join(ans))