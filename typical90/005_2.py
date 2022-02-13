mod = 10 ** 9 + 7


def multiply(matrix_A, matrix_B, b):
    matrix_C = [[0 for _ in range(b)] for __ in range(b)]
    for i in range(b):
        for j in range(b):
            for k in range(b):
                matrix_C[i][k] += matrix_A[i][j] * matrix_B[j][k]
                matrix_C[i][k] %= mod
    return matrix_C


def power_matrix(matrix, n, b):
    matrix_array = []
    matrix_array.append(matrix)
    for i in range(62):
        matrix_array.append(multiply(matrix_array[-1], matrix_array[-1], b))
    ans = [[0 for i in range(b)] for _ in range(b)]
    for i in range(b):
        ans[i][i] = 1
    for i in range(62, -1, -1):
        if n & (1 << i):
            ans = multiply(ans, matrix_array[i], b)
    return ans


n, b, k = map(int, input().split())
c = list(map(int, input().split()))

matrix = [[0 for _ in range(b)] for __ in range(b)]
for i in range(b):
    for j in range(k):
        nex = (i * 10 + c[j]) % b
        matrix[i][nex] += 1
ans = power_matrix(matrix, n, b)
print(ans[0][0])