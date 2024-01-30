m = int(input())
ten = []
five = []
one = []
def cn(ca, n, cash):
    cu = ca // n 
    cash.append(cu)
    return ca - cu * n
m = cn(m, 10, ten)
m = cn(m, 5, five)
m = cn(m, 1, one)
print(ten[0], " coins of ten, ", five[0], " coins of five, ", one[0], " coins of one.")
