from collections import Counter

s = input()
t = input()

counter_s = dict(Counter(s))
counter_t = dict(Counter(t))
atcoder_string_set = set('atcoder')

for s_key, s_value in counter_s.items():
    if s_key == '@':
        continue
    if s_key not in counter_t:
        if s_key not in atcoder_string_set:
            print('No')
            exit()
        if s_key in atcoder_string_set:
            if '@' not in counter_t:
                print('No')
                exit()
            else:
                counter_t['@'] -= s_value
                if counter_t['@'] == 0:
                    counter_t.pop('@')
                elif counter_t['@'] < 0:
                    print('No')
                    exit()
    elif s_key in counter_t:
        if s_value <= counter_t[s_key]:
            counter_t[s_key] -= s_value
            if counter_t[s_key] == 0:
                counter_t.pop(s_key)
        else:
            remained_value = s_value - counter_t[s_key]
            counter_t.pop(s_key)
            if s_key not in atcoder_string_set:
                print('No')
                exit()
            if s_key in atcoder_string_set:
                if '@' not in counter_t:
                    print('No')
                    exit()
                else:
                    counter_t['@'] -= remained_value
                    if counter_t['@'] < 0:
                        print('No')
                        exit()
for t_key, t_value in counter_t.items():
    if t_key not in atcoder_string_set and t_key != '@':
        print('No')
        exit()        

print('Yes')