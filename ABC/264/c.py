import numpy as np
from itertools import combinations
from copy import copy

ha, wa = map(int, input().split())
array = []
for i in range(ha):
    array.append(list(map(int, input().split())))
array_a = np.array(array)
    
hb, wb = map(int, input().split())
array = []
for i in range(hb):
    array.append(list(map(int, input().split())))
array_b = np.array(array)

if hb > ha or wb > wa:
    print("No")
    exit()

for rows in combinations(range(ha), hb):
    for columns in combinations(range(wa), wb):
        rows = set(rows)
        columns = set(columns)
        row_tf = [True if i in rows else False for i in range(ha)]
        column_tf = [True if i in columns else False for i in range(wa)]
        tmp = array_a[np.ix_(row_tf, column_tf)]
        if np.array_equal(tmp, array_b):
            print("Yes")
            exit()
print("No")