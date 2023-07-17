n = input()
int_n = int(n)

if int_n <= 10 ** 3 - 1:
    print(n)
    exit()

digit = len(n)

base = 10 ** (digit - 3)

print(int_n // base * base)