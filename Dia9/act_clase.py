def calcular_definitiva(lista):
    lista[0]=lista[0]
    lista[1]=lista[1]
    lista[2]=lista[2]
    sumatoria=0
    for i in range(len(lista)):
        sumatoria=sumatoria+lista[i]

    return sumatoria


for i in range(5):
    print("Estudiante#",i+1)
    lista=[]
    notaMayor=0
    definitiva=0
    for i in range(3):
        if(i==2):
            numerito=(float(input("Ingresa tu nota:")))
            print(numerito)
            definitiva=definitiva+(numerito*0.4)
            if(numerito>notaMayor):
                notaMayor=numerito
            lista.append(numerito)
        else:
            numerito=(float(input("Ingresa tu nota:")))
            print(numerito)
            definitiva=definitiva+(numerito*0.3)
            if(numerito>notaMayor):
                notaMayor=numerito
            lista.append(numerito)
    definitiva=calcular_definitiva(lista)
    print("Tu nota mayor es:",notaMayor)
    print("Tu definitiva es:",definitiva)
    if(definitiva<2):
        print("Perdiste tu vida.")
    elif (definitiva<3):
        print("Pues... todo bien...recupera")
    elif(definitiva>4.5):
        print("Excelente estudiante! Sos ejemplar")

#Catalina Mulford Monroy
    