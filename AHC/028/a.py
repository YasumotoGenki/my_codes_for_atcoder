# input
n, m = map(int, input().split())
si, sj = map(int, input().split())
keyboard = []
happy_words = []
for _ in range(n):
    keyboard.append(input())
for _ in range(m):
    happy_words.append(input())

# 文字列->マスの辞書作成
word2cell = dict()
for h in range(n):
    for w in range(n):
        if keyboard[h][w] not in word2cell:
            word2cell[keyboard[h][w]] = []
        word2cell[keyboard[h][w]].append([h, w])

# TODO: 連続している文字列チェック
# TODO: 各マスから遷移できる文字列コスト把握

# 貪欲方的にまだ部分文字列として採用していないtを採用していく
for i in range(m):
    current_word = happy_words[i]
    for j in range(5):
        cost = 10000
        for x, y in word2cell[current_word[j]]:
            if cost > abs(si - x) + abs(sj - y):
                cost = abs(si - x) + abs(sj - y)
                next_x, next_y = x, y
        si = next_x
        sj = next_y
        print(si, sj)
