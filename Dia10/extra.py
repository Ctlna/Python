import json
dici=open("data.json")
pausar=json.load(dici)

#Leer
print(pausar)

#crear/actualizar
t=pausar["ventas"]["clientes"]
nuevito=input("Por favor ingrese los siguientes datos separados por comas: id, nombre, apellido, ciudad, categoría\n").split(",")
t.append(nuevito)
print(t)
with open("data.json", "w") as file:
    json.dump(pausar, file)

#Eliminar
ventas = pausar["ventas"]
pedidos = ventas["pedidos"]
eliminar = input("Fila a eliminar: ")
nuedos = [pedido for pedido in pedidos if eliminar not in pedido]
ventas["pedidos"] = nuedos
with open("data.json", "w") as file:
    json.dump(pausar, file)
print(pausar)

