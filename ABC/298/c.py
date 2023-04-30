import heapq

n = int(input())
q = int(input())

num_2_box_list = [[] for _ in range(10 ** 5 * 2 + 1)]
box_content_list = [[] for _ in range(10 ** 5 * 2 + 1)]

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i, j = query[1], query[2]
        heapq.heappush(box_content_list[j], i)
        heapq.heappush(num_2_box_list[i], j)
    elif query[0] == 2:
        i = query[1]
        stack = []
        while(box_content_list[i]):
            card = heapq.heappop(box_content_list[i])
            stack.append(str(card))
        print(" ".join(stack))
        for item in stack:
            heapq.heappush(box_content_list[i], int(item))
    else:
        i = query[1]
        done_set = set()
        stack = []
        while(num_2_box_list[i]):
            card = heapq.heappop(num_2_box_list[i])
            if card not in done_set:
                stack.append(str(card))
                done_set.add(card)
        print(" ".join(stack))
        for item in stack:
            heapq.heappush(num_2_box_list[i], int(item))