n, q = map(int, input().split())
user_follow_dict = dict()
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if a not in user_follow_dict:
            user_follow_dict[a] = set()
        user_follow_dict[a].add(b)
    elif t == 2:
        if a not in user_follow_dict:
            pass
        else:
            if b in user_follow_dict[a]:
                user_follow_dict[a].remove(b)
    else:
        if a in user_follow_dict and b in user_follow_dict:
            if b in user_follow_dict[a] and a in user_follow_dict[b]:
                print("Yes")
            else:
                print("No")
        else:
            print("No")