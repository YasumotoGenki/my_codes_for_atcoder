s = input()
t = input()
s_0 = ord(s[0]) - ord("A")
s_1 = ord(s[1]) - ord("A")
t_0 = ord(t[0]) - ord("A")
t_1 = ord(t[1]) - ord("A")

length_s = abs(s_0 - s_1)
if s_0 == 0:
    length_s = min(length_s, abs(5 - s_1))
elif s_1 == 0:
    length_s = min(length_s, abs(5 - s_0))
length_s = min(length_s, 2)

length_t = abs(t_0 - t_1)
if t_0 == 0:
    length_t = min(length_t, abs(5 - t_1))
elif t_1 == 0:
    length_t = min(length_t, abs(5 - t_0))
length_t = min(length_t, 2)

if length_s == length_t:
    print("Yes")
else:
    print("No")