#ejercicio1
def jeje():
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

#ejercicio2
def negate(num):
    return -num
def large_num(num):
    if (num>10000):
        print("True")
    else:
        print("False")
        
#ejercicio3
def ball_collide(l,a,x):
    sumr=l+a
    if x<=sumr:
        print(True)
    else:
        print(False)
