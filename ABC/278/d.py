n = int(input())
a = list(map(int, input().split()))
q = int(input())

all_elements = None
current_element_dict = dict()

for i in range(q):
    query_list = list(map(int, input().split()))
    if query_list[0] == 1:
        all_elements = query_list[1]
        current_element_dict = dict()
    elif query_list[0] == 2:
        if query_list[1] in current_element_dict:
            current_element_dict[query_list[1]] += query_list[2]
        else:
            current_element_dict[query_list[1]] = query_list[2]
    else:
        if query_list[1] in current_element_dict:
            if all_elements:
                print(current_element_dict[query_list[1]] + all_elements)
            else:
                print(current_element_dict[query_list[1]] + a[query_list[1] - 1])
        elif all_elements is not None:
            print(all_elements)
        else:
            print(a[query_list[1] - 1])
