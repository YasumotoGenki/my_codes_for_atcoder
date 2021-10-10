n, m = map(int, input().split())
list_a = []
for i in range(2 * n):
    list_a.append(input())

def janken(hand_a, hand_b):
    if hand_a == hand_b:
        return 'aiko'
    elif hand_a == 'G' and hand_b == 'C':
        return 'win'
    elif hand_a == 'C' and hand_b == 'P':
        return 'win'
    elif hand_a == 'P' and hand_b == 'G':
        return 'win'
    else:
        return 'lose'

# due to sorted fanction, I use REVERSED index
score_sheet = [[0, 2 * n - i] for i in range(2 * n)]
for round_i in range(m):
    for first_person_ssi in range(0, 2 * n, 2):
        second_person_ssi = first_person_ssi + 1
        first_person_i = 2 * n - score_sheet[first_person_ssi][1]
        second_person_i = 2 * n - score_sheet[second_person_ssi][1]
        
        first_person_hand = list_a[first_person_i][round_i]
        second_person_hand = list_a[second_person_i][round_i]
        game_result = janken(first_person_hand, second_person_hand)
        if game_result == 'aiko':
            pass
        elif game_result == 'win':
            score_sheet[first_person_ssi][0] += 1
        else:
            score_sheet[second_person_ssi][0] += 1
    score_sheet = sorted(score_sheet, key=lambda x: (x[0], x[1]), reverse=True)

for i in range(2 * n):
    print(2 * n - score_sheet[i][1] + 1)

