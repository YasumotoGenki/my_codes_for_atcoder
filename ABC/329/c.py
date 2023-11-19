n = int(input())
s = input()

prev = s[0]
count = 1
character2count_dict = dict()
for i in range(1, n):
    if s[i] == prev:
        count += 1
    else:
        if prev not in character2count_dict:
            character2count_dict[prev] = count
        else:
            character2count_dict[prev] = max(character2count_dict[prev], count)
        count = 1
    prev = s[i]
else:
    if prev not in character2count_dict:
            character2count_dict[prev] = count
    else:
        character2count_dict[prev] = max(character2count_dict[prev], count)
ans = 0
for key, value in character2count_dict.items():
    ans += value
print(ans)