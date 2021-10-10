LETTERS = "abcdefghijklmnopqrstuvwxyz"

def making_normal_string(name, x):
    normal_name = ""
    for c in name:
        idx = x.index(c)
        normal_name += LETTERS[idx]
    return normal_name


x = input()
n = int(input())
s = []
for i in range(n):
    letters = input()
    normal_letters = making_normal_string(letters, x)
    s.append([normal_letters, letters])

s = sorted(s, key=lambda x : x[0])
for i in range(n):
    print(s[i][1])