def calc_money(a,b,c):
    if(a == b == c):
        return 10000 + 1000*a
    elif(a == b):
        return 1000 + 100*a
    elif(c == b):
        return 1000 + 100*b
    elif(a == c):
        return 1000 + 100*a
    else:
        return max(a,b,c)*100 

print(calc_money(2,3,4))