n = int(input())
s = list(input())

is_bracketed_characters = False

for i in range(n):
    if s[i] == '"':
        is_bracketed_characters = not is_bracketed_characters
    else:
        if not is_bracketed_characters and s[i] == ',':
            s[i] = '.'

print("".join(s))