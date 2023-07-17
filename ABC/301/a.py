n = int(input())
s = input()

count_A = s.count('A')
count_T = s.count('T')

if count_A > count_T:
    print('A')
elif count_T > count_A:
    print('T')
else:
    if s[-1] == 'A':
        print('T')
    else:
        print('A')