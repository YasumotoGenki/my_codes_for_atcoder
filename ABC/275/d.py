from math import floor

N = int(input())

table = dict()
table[0] = 1

def f(n):
    global table
    next_2_div = floor(n / 2)
    next_3_div = floor(n / 3)
    if n == 0:
        return 1
    if next_2_div not in table:
        table[next_2_div] = f(next_2_div)
    if next_3_div not in table:
        table[next_3_div] = f(next_3_div)
    return table[next_2_div] + table[next_3_div]

print(f(N))