n = int(input())
c = str(bin(n))
idx = -1
count = 0
while(True):
    if c[idx] == "0":
        count += 1
        idx -= 1
    else:
        break
print(count)