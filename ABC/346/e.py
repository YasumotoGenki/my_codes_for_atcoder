h, w, m = map(int, input().split())
query = []
row_query = []
column_query = []
for _ in range(m):
    t, a, x = map(int, input().split())
    query.append([t, a, x])

left_cell_num = h * w
answer_dict = dict()
row_query_count, column_query_count = 0, 0
done_row_set, done_column_set = set(), set()
done_flg = False

for t, a, x in reversed(query):
    if t == 1:
        if a not in done_row_set:
            done_row_set.add(a)
            row_query_count += 1
            if (w - column_query_count) == 0:
                continue
            if x not in answer_dict:
                answer_dict[x] = 0
            answer_dict[x] += (w - column_query_count)
            left_cell_num -= (w - column_query_count)
    else:
        if a not in done_column_set:
            done_column_set.add(a)
            column_query_count += 1
            if h - row_query_count == 0:
                continue
            if x not in answer_dict:
                answer_dict[x] = 0
            answer_dict[x] += (h - row_query_count)
            left_cell_num -= (h - row_query_count)

if left_cell_num > 0:
    if 0 not in answer_dict:
        answer_dict[0] = 0
    answer_dict[0] += left_cell_num

print(len(answer_dict))
for key in sorted(answer_dict.keys()):
    print(key, answer_dict[key])
