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
orden=[]
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
ListaDel2017 = []
for j in pausar["ventas"]["pedidos"]:
    if "2017" in pausar["ventas"]["pedidos"][cont]["fecha"]:
        if pausar["ventas"]["pedidos"][cont]["total"] > 500:
            ListaDel2017.append(j)
        cont += 1
    else:
        cont += 1

print(ListaDel2017)

# 5. comerciales que tienen una comisión entre 0.05 y 0.11
print("")
cont=0
comin=[]
for j in pausar["ventas"]["comerciales"]:
    if 0.05<=pausar["ventas"]["comerciales"][cont]["comisión"]<=0.11 :
            comin.append(j)
            cont += 1
    else:
            cont += 1
print(comin)

# 6. valor comisiòn màs alta
print("")
MValor=[]
for i in pausar["ventas"] ["comerciales"] :
    MValor.append(i["comisión"])
MValor.sort()
MValor.reverse()
print(MValor[0])

# 7. Ciudad: Sevilla/orden
print("")
guar=[]
j = pausar["ventas"]["clientes"]
orden = sorted(j, key=itemgetter("ciudad"))
for j in orden: 
    if j["ciudad"] == "Sevilla":  
        guar.append(j)
guar.sort(key=itemgetter("nombre", "apellido1") ) 
print(guar)

# 8. 
print("")
namE=[]
for i in pausar["ventas"]["clientes"] :
    if i["nombre"].startswith("A") and i["nombre"].endswith("n"):
        namE.append(i["nombre"])
    elif i["nombre"].startswith("P"):
        namE.append(i["nombre"])
namE.sort() 
print(namE)

# 9. 
print("")
nomb=[]
for i in pausar["ventas"]["clientes"] :
    if i["nombre"].startswith("A"):
        nomb.append(i["nombre"])
nomb.sort() 
print(nomb)

# 10. Ruiz
print("")
ape=[]
k = pausar["ventas"]["comerciales"]
orden = sorted(k, key=itemgetter("apellido1"))
for j in orden: 
    if j["apellido1"] == "Ruiz":  
        ape.append(j)
ape.sort(key=itemgetter("nombre", "apellido1") ) 
print(ape)

#Catalina Mulford Monroy
