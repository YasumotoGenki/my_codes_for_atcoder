L, R = map(int, input().split())
s = input()

print(s[:L-1] + s[L-1:R][::-1] + s[R:])