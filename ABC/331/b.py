N, S, M, L = map(int, input().split())

ans = 10 ** 100
for s in range(N // 6 + 2):
    for m in range(N // 8 + 2):
        for l in range(N // 12 + 2):
            if s * 6 + m * 8 + l * 12 >= N:
                ans = min(ans, s * S + m * M + l * L)

print(ans)