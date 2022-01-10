n = int(input())

if n >= 42:
    print("AGC{:0=3}".format(n + 1, '03x'))
else:
    print("AGC{:0=3}".format(n, '03x'))