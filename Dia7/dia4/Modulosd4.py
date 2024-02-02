def C(x, ye):
    for i in range(x):
        n = int(input())
        ye.append(n)

def T(x, ye):
    for i in range(x):
        n = int(input())
        ye.append(n)

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)



#Catalina Mulford Monroy
#Daniela Forero Ballen