from collections import Counter
s = list(input())
counter = Counter(s)
has_uppercase = False
has_lowercase = False
for key, value in counter.items():
    if value > 1:
        print("No")
        exit()
    if key.isupper():
        has_uppercase = True
    if key.islower():
        has_lowercase = True
if has_lowercase and has_uppercase:
    print("Yes")
else:
    print("No")
