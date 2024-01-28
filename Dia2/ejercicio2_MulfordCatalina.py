import random

z = random.randint(1,100)
#print(z)
print("Adivina el número, solo tendras 10 intentos.")
q=10

for _ in range(1,q):
    n=int(input("Pon un número"))
    if n == z:
        print("Felicidades! ganaste, lo hiciste en", q, "intentos")
        break
    elif n < z:
        print("El número que buscas es mayor")
    elif n > z:
        print("El número que buscas es menor")

else:
    print("Lo siento, has agotado tus 10 intentos. El número correcto era: ",z)