h, w = map(int, input().split())
a = []
for _ in range(h):
    cur_line_element_list = list(map(int, input().split()))
    cur_ans = ""
    for idx in range(w):
        if cur_line_element_list[idx] == 0:
            cur_ans += "."
        else:
            cur_ans += chr(cur_line_element_list[idx] + ord('A') - 1)
    print(cur_ans)

