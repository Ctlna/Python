import Modulosd2

print("Fibonacci es una secuencia comienza con 0 y 1, y cada término subsiguiente es la suma de los dos términos anteriores.")
n = int(input("Cuantas veces deseas que se repita el proceso:"))
num1 = 0
num2 = 1
print(num1)
print(num2)
s = 1
while s==1:
    for i in range(0,n-1):
           i=num1+num2
           print(i)
           num1=num2
           num2=i
    s=int(input("¿Deseas seguir? (Si: 1, No: 0): "))
    Modulosd2.segui(s)
#1Seguir-0Parar