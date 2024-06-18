s = input()

lowercase_count = 0
uppercase_count = 0

for i in range(len(s)):
    if s[i].isupper():
        uppercase_count += 1
    else:
        lowercase_count += 1

if uppercase_count > lowercase_count:
    print(s.upper())
else:
    print(s.lower())