n, x = map(int, input().split())
a = list(map(int, input().split()))

know_people_set = set()
know_people_set.add(x)

que = []
que.append(x)
while(que):
    cur_person_id = que.pop()
    cur_person_id -= 1
    next_person_id = a[cur_person_id]
    if next_person_id not in know_people_set:
        know_people_set.add(next_person_id)
        que.append(next_person_id)
print(len(know_people_set))
