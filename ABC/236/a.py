def list2str(ls):
    return "".join(ls)

s = list(input())
a, b = map(int, input().split())
str_a = s[a - 1]
str_b = s[b - 1]
s[a - 1] = str_b
s[b - 1] = str_a
print(list2str(s))