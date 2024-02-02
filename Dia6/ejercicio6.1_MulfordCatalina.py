def negate(num):
    return -num
def large_num(num):
    if (num>10000):
        print("True")
    else:
        print("False")

b=int(input())

neg_b=negate(b)
print("b:",b,"neg_b:",neg_b)

big=large_num(b)


# 1. b no estaba definida
# 2. las variables para llamar al número negatico estaban mal, junto con el orden.
# 3. la función de mayor a 10000 no tenia bien escrito lo que se retornaria.
#Catalina Mulford Monroy 
