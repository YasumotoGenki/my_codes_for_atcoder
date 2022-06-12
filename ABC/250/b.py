n, a, b = map(int, input().split())
ans = ["" for _ in range(a * n)]
for i in range(n):
    for j in range(a):
        for k in range(n * b):
            if i % 2 == 0:
                if k % (2 * b) < b:
                    ans[i * a + j] += "."
                else:
                    ans[i * a + j] += "#"
            else:
                if k % (2 * b) < b:
                    ans[i * a + j] += "#"
                else:
                    ans[i * a + j] += "."
for item in ans:
    print(item)
