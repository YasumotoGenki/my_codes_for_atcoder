s = input()

rev_pointer = len(s) - 1
pointer = 0

while(pointer <= rev_pointer):
    if pointer == rev_pointer:
        print("Yes")
        exit()
    if s[pointer] != s[rev_pointer]:
        if s[rev_pointer] != "a":
            print("No")
            exit()
        else:
            rev_pointer -= 1
    else:
        pointer += 1
        rev_pointer -= 1

print("Yes")
