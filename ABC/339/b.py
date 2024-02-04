h, w, n = map(int, input().split())
field_list = [["." for _ in range(w)] for _ in range(h)]
current_position = [0, 0]
direction = "u"
for i in range(n):
    x, y = current_position
    if x == h:
        x = 0
    if x < 0:
        x = h - 1
    if y == w:
        y = 0
    if y < 0:
        y = w - 1

    if field_list[x][y] == ".":
        field_list[x][y] = "#"
        if direction == "u":
            direction = "r"
            current_position = [x, y + 1]
        elif direction == "r":
            direction = "d"
            current_position = [x + 1, y]
        elif direction == "d":
            direction = "l"
            current_position = [x, y - 1]
        elif direction == "l":
            direction = "u"
            current_position = [x - 1, y]
    else:
        field_list[x][y] = "."
        if direction == "u":
            direction = "l"
            current_position = [x, y - 1]
        elif direction == "r":
            direction = "u"
            current_position = [x - 1, y]
        elif direction == "d":
            direction = "r"
            current_position = [x, y + 1]
        elif direction == "l":
            direction = "d"
            current_position = [x + 1, y]

for i in range(h):
    print("".join(field_list[i]))