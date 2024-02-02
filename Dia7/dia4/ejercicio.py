import Modulosd4
cont=bool

while cont:
    legita=[]
    coins = []
    table = []
    cosito = input()
    cc, ct = map(int, cosito.split())

    if cc == 0 and ct == 0:
        cont = False
    else:
        Modulosd4.C(cc, coins)
        Modulosd4.T(ct, table)

        if 4 <= len(coins) <= 50:
            pass  
        else:
            exit()

        if 1 <= len(table) <= 10:
            pass 
        else:
            exit()
    mcd = Modulosd4.mcd(cc, ct)
    mcm = Modulosd4.mcm(cc, ct)
print(mcm,mcd)
   