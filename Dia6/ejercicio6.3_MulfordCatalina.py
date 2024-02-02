def ball_collide(l,a,x):
    sumr=l+a
    if x<=sumr:
        print(True)
    else:
        print(False)

#cosito1
xbu=int(input())
ybu=int(input())
r=int(input())
rau=2*r

#cosito2
xpt=int(input())
ypt=int(input())
dio=int(input())
rtw=2*dio

di=((xpt-xbu)**2 + (ypt-ybu)**2)**0.5
ball_collide(rau,rtw,di)
#Catalina Mulford Monroy 
