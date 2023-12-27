n = int(input())

count = 1
candidate = ["3"]
digit = 2

def dfs(current_str, limit):
    global candidate
    if len(current_str) == limit - 1:
        candidate.append(current_str + "3")
        return
    for j in range(int(current_str[-1]), 4):
        dfs(current_str + str(j), limit)

while(len(candidate) < 333):
    for i in range(1, 4):
        dfs(str(i), digit)
    digit += 1
print(candidate[n - 1])