m = int(input())
ten = []
five = []
one = []

def cos(m, n):
    d = m - n
    return (d)

while m >= 10:
    cos(m, 10)
    ten.append(+1)
    while 5 <= m < 10:
        cos(m, 5)
        five.append(+1)
        while m < 5:
            cos(m, 1)
            one.append(+1)

print(ten, "coins of ten,", five, "coins of five,", one, "coins of one.")