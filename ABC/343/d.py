n, t = map(int, input().split())
count_dict = dict()
person_count_list = [0 for _ in range(n)]
count_dict[0] = n
for _ in range(t):
    a, b = map(int, input().split())
    a -= 1
    previous_count = person_count_list[a]
    person_count_list[a] += b
    after_count = person_count_list[a]
    if previous_count in count_dict:
        count_dict[previous_count] -= 1
        if count_dict[previous_count] == 0:
            count_dict.pop(previous_count)
    if after_count not in count_dict:
        count_dict[after_count] = 0
    count_dict[after_count] += 1
    print(len(count_dict))