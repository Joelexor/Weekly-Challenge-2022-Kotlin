#Reto semanal 31: Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.

def añosBisiestos():
    año=int(input("Introduce un año: "))
    for i in range(30):
        año+=4
        if (año%4 == 0 and (año%100 != 0 or año%400 == 0)):
            print("Num",i+1,":",año)
        elif(año%4 != 0):
            año-=año%4
            if(año%100 == 0):
                año+=4
            print("Num",i+1,":",año)
        else:
            año+=4
            print("Num",i+1,":",año)

añosBisiestos()