s = input()

left_b_idx = s.index('B')
right_b_idx = s.rindex('B')
if left_b_idx % 2 == right_b_idx % 2:
    print("No")
    exit()

if s.index('R') < s.index('K') < s.rindex('R'):
    print("Yes")
else:
    print("No")