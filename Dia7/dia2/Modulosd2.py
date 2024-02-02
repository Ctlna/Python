#ejercicio1
def segui(s):
    
    if s == 0:
        s = 0
    elif s==1:
        s=1
        
#ejercicio2
def lazar(s,f):
    for _ in range(1,f):
        m=int(input("Pon un número"))
        if m == s:
            print("Felicidades! ganaste, lo hiciste en", f, "intentos")
            break
        elif m < s:
            print("El número que buscas es mayor")
        elif m > s:
            print("El número que buscas es menor")

    else:
        print("Lo siento, has agotado tus 10 intentos. El número correcto era: ",s)
        
