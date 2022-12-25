s = input()
idx = 0
count = 0
while(idx < len(s)):
    if s[idx] == '0' and idx + 1 < len(s) and s[idx + 1] == '0':
        idx += 1
    idx += 1
    count += 1
print(count)