n  = input()

num_ch= ""
for i in range(len(n)):
    if num_ch == "":
        num_ch = n[i]
    else:
        if int(num_ch) > int(n[i]):
            num_ch = n[i]
        else:
            print("No")
            exit()

print("Yes")