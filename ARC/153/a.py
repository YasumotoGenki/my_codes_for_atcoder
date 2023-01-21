n = int(input())
ans = ""
count = 0

for i in range(1, 10):
    if count + 10 ** 5 < n:
        count += 10 ** 5
    else:
        ans += str(i)
        ans += str(i)
        break

for i in range(10):
    if count + 10 ** 4 < n:
        count += 10 ** 4
    else:
        ans += str(i)
        break

for i in range(10):
    if count + 10 ** 3 < n:
        count += 10 ** 3
    else:
        ans += str(i)
        break

for i in range(10):
    if count + 10 ** 2 < n:
        count += 10 ** 2
    else:
        ans += str(i)
        ans += str(i)
        break

for i in range(10):
    if count + 10 < n:
        count += 10
    else:
        ans += str(i)
        last_str = str(i)
        break

for i in range(10):
    if count + 1 < n:
        count += 1
    else:
        ans += str(i)
        break

ans += last_str
print(ans)