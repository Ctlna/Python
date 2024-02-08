#import datetime
import json
dici=open("data.json")
pausar=json.load(dici)
#print(pausar)


# CREAR UN CRUD (CREACION,LECTURA,ACTUALIZACIÓN Y ELIMINACIÓN) DE LOS 3 CONJUNTOS DE DATOS ADENTRO DE DATA.JSON, LOS CUALES DEBEN SER PERSISTENTES DONDE APLIQUE.

#crear
t=pausar["ventas"]["clientes"]
print("id-nombre-apellido1-ciudad-categoría (Pon las categorias tu mismo)")
nuevito=input("")
t.append(nuevito)
with open("data.json", "w") as file:
    json.dump(pausar, file)

#actualizar
print("")
a=pausar["ventas"]["comerciales"]
print("id-nombre-apellido1-ciudad-categoría")
cambiar=input("")
a.append(cambiar["id_cliente"][0])
with open("data.json", "w") as file:
    json.dump(pausar, file)                                               
print(a)
#eliminar


#leer
print("")
print(pausar)
