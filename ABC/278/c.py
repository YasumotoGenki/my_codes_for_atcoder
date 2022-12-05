n, q = map(int, input().split())

follower_dict = dict()

for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if a not in follower_dict:
            follower_dict[a] = set()
        follower_dict[a].add(b)
    elif t == 2:
        if a in follower_dict:
            if b in follower_dict[a]:
                follower_dict[a].discard(b)
    else:
        if a in follower_dict and b in follower_dict[a] and b in follower_dict and a in follower_dict[b]:
            print("Yes")
        else:
            print("No")
            