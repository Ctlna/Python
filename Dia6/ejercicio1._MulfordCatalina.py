#REALIZAR UN PROGRAMA QUE USE UN DICCIONARIO PARA GESTIONAR LOS PRODUCTOS Y PRECIOS DE LA TABLA, 
#DONDE SE LE PREGUNTE AL USUARIO POR UN PRODUCTO Y LA CANTIDAD. AL FINALIZAR MOSTRAR EN LA CONSOLA 
#EL PRECIO TOTAL. SI EL PRODUCTO NO ESTA DEBE MOSTRAR UN MENSAJE INFORMANDO SOBRE ELLO

diccionario={"arena":7500,"gravilla": 6800,
       "granito":40600,"cemento": 30990}

for i in diccionario:
    print(i)

for valor in diccionario:
    pre=(diccionario[valor])

producto=input("que producto deseas?(escribe tal cual)")
cant=int(input("cuantos paquetes llevas?(Solo nùmero)"))

variableConsulta= diccionario[producto]

valorFinal = variableConsulta* cant
print(f"EL valor total del produto {producto} será de: {valorFinal}")

#Catalina Mulford Monroy 
