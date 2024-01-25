##---------------------- ------ - -
##---- Ejercicio 1
##---------------------- ------ - -
## Impresiòn en consola
print("Hola estrellitas"); 


# --- Datos primitivos -------
#1. String
texto="campusand"
print(texto)
print(type (texto))
#2. int
numeroEntero=1
print(numeroEntero)
#3. float
numeroDecimal=9.1
print(numeroDecimal)
#4. Boolean
boleano=True
print(boleano)
#5. Dooble
numeroDecimalLargo=3,1416784541112136952
print(numeroDecimalLargo)

# --- Entradas por parte del usuario ---
entradaUsuario =  input("Ingresa tu nombre: ")
print("Tu nombre es: ", entradaUsuario)

# --- Entradas por parte del usuario con definiciòn de tipo de dato primitivo---
entradaUsuarioNumero =  input("Ingresa tu edad: ")
numeroFinal=int(entradaUsuarioNumero)
print("Tu edad es: ", numeroFinal)


# ----Ciclos----
#Ciclo for
for i in range(5,10,2):#for contador in range(desde,hasta,pasos):
    print(i)
#Ciclo while
boleanito = True
while boleanito==True:#While condiciòn_a_cumplir :
    print("Sobreviviendo")
    boleanito=False


# ----Condicionales---
texto1="campus"
if texto1=="campus":
    print("soy campus")
else:
    print("No soy campus")


## Desarrollado por Catalina Mulford Monroy - 1097490150