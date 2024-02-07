import datetime
import json
dici=open("data.json")
pausar=json.load(dici)

# 1. Pedidos (del más reciente al más viejo):
print("")
from operator import itemgetter
t = pausar["ventas"]["pedidos"]
orden = sorted(t, key=itemgetter("fecha"), reverse=True)
print(orden)

# 2. Los 2 de màs valor
print("")
from operator import itemgetter
orden=[]
t = pausar["ventas"]["pedidos"]
orden = sorted(t, key=itemgetter("total"), reverse=True)
print(orden[0],orden[1])

# 3. Clientes que pidieron
print("")
iden=[]
for j in pausar["ventas"] ["pedidos"]:
    iden.append(j["id_cliente"])
iden = list(set(iden)) 
print(iden)

# 4. año 2017 >500
print("")
cont=0
Lista2017 = []
for j in pausar["ventas"]["pedidos"]:
    if "2017" in pausar["ventas"]["pedidos"][cont]["fecha"]:
        if pausar["ventas"]["pedidos"][cont]["total"] > 500:
            Lista2017.append(j)
        cont += 1
    else:
        cont += 1

print(Lista2017)

# 5. comerciales que tienen una comisión entre 0.05 y 0.11
print("")

# 6. valor comisiòn màs alta
print("")
MValor=[]
for i in pausar["ventas"] ["comerciales"] :
    MValor.append(i["comisión"])
MValor.sort()
MValor.reverse()
print(MValor[0])