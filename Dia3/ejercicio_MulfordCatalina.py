##Catalina Mulford Monroy P1
m = int(input())
ten = []
five = []
one = []
def cn(ca, n, cash):
    cash.append(ca // n)
    return ca - (ca // n) * n
m = cn(m, 10, ten)
m = cn(m, 5, five)
m = cn(m, 1, one)
print(ten[0],  five[0],  one[0])
