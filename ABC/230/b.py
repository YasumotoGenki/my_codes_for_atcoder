s = input()

pre_c = ""
cur_c = ""
count = 0
for i in range(len(s)):
    cur_c = s[i]
    if pre_c == "":
        pre_c = cur_c
        count += 1
    else:
        if pre_c == "o":
            if cur_c == "o":
                print("No")
                exit()
            else:
                count = 1
                pre_c = cur_c
        else: # if pre_c == "x"
            if cur_c == "x" and count >= 2:
                print("No")
                exit()
            elif cur_c == "x" and count <= 1:
                count += 1
                pre_c = cur_c
            elif cur_c == "o":
                if count == 2:
                    pass
                else:
                    if i <= 1:
                        pass
                    else:
                        print("No")
                        exit()
                count = 1
                pre_c = cur_c

print("Yes")