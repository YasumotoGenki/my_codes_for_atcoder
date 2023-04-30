n = int(input())
s = input()

if s.index("|") < s.index("*") < s.rindex("|"):
    print("in")
else:
    print("out")