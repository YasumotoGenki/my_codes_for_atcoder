from itertools import product

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 


N = int(input())

kakko_list = product(["(", ")"], repeat=N)

ans = []
for item in kakko_list:
    count = 0
    for i in range(N):
        if item[i] == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    else:
        if count == 0:
            print(listToString(item))