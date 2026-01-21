# app de banco simple solo para aprender 
# Desarrollado en python con la libreria de tkinter para hacer una interfaz


#Codigo desarrollado por Awioon



from tkinter import *







dinero = 100

intentos = [3,2,1,0]

print("Bienvenido al banco")




for i in intentos:
        pin = int(input("Introduce su pin:"))  
        if pin==1234:
            print("Bienvenido a tu banco")
            break
                           

        if pin!=1234:
            print("Pin Incorrecto")
            print("Le quedan:",i,"Intentos")
        elif i==0:
            break


while True:
    print("1. Ingresar\n2. Retirar\n3. Ver saldo\n4. Salir")
    eleccion=input("Que quieres hacer:")


    if(eleccion=="1"):
        ingresar = int(input("Cuanto deseas ingresar:"))
        operacion1=ingresar+dinero
        dinero=operacion1
        print("Ahora tienes en el banco:",dinero)
        break


    elif(eleccion=="2"):
        retirar = int(input("Cuanto deseas retirar:"))
        operacion2=dinero-retirar
        dinero=operacion2
        print("Ahora tienes en el banco:",dinero)
        break


    elif(eleccion=="3"):
         print("Este es tu saldo:",dinero)
         break
    
         
    elif(eleccion=="4"):
         print("Adios muchas gracias")
         break
        
