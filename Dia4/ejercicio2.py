def C(x,coins):
    for i in range(x):
        n=int(input())
        if 4<=n<=50:
            coins.append[n]
        else:
            exit()
def T(x,table):
    for i in range(1,x):
        n=int(input())
        if 1<=n<=10:
            table.append[n]
        else:
            exit()
def calcu(lc, lt, List_coins):
    result = []

    for i in range(lc):
        set_list = List_coins[i * lt : (i + 1) * lt]
        length = sum(set_list[:lt // 2]) - sum(set_list[lt // 2:])
        gleg = max(x for x in set_list if x <= length)
        smalleg = min(x for x in set_list if x >= length)
        result.append((gleg, smalleg))
    return result

cont=True

while cont:
    coins=()
    table=[]
    cosito=input()
    cc, ct = map(int, cosito.split())
    if  cc==0 and ct==0:
        cont=False
    else:
       C(cc,coins)
       T(ct,table)
    output = calcu(cc, ct, coins)
    for leles in output:
     print(f"{leles[0]} {leles[1]}")
   
#Catalina Mulford Monroy
#Daniela Forero 