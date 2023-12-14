n = int(input())
s = []
for i in range(n):
    line = list(input())
    tmp = []
    for item in line:
        if item == "o":
            tmp.append(True)
        else:
            tmp.append(False)
    s.append(tmp)
row_count_list = []
column_count_list = []
for i in range(n):
    count_row = 0
    count_column = 0
    for j in range(n):
        if s[i][j]:
            count_row += 1
        if s[j][i]:
            count_column += 1
    row_count_list.append(count_row)
    column_count_list.append(count_column)

ans = 0
for i in range(n):
    for j in range(n):
        if s[i][j] and row_count_list[i] > 1 and column_count_list[j] > 1:
            ans += (row_count_list[i] - 1) * (column_count_list[j] - 1)
print(ans)