w, b = map(int, input().split())
kenban = "wbwbwwbwbwbw" * 22

flg = False
for i in range(15):
    if kenban[i:i+w+b].count('b') == b and kenban[i:i+w+b].count('w') == w:
        print("Yes")
        exit()
print("No")