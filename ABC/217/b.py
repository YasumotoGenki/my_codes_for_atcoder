contests = set(["ABC", "ARC", "AGC", "AHC"])
candidates = set()
for i in range(3):
    candidates.add(input())
ans = list(contests - candidates)[0]
print(ans)