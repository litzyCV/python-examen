operar = 0
usuario = ""
clave = ""
login = False
while operar != 2:
    print("1) operar cajero")
    print("2) cerrar cajero")
    print("1) seleccionar una opcion")
    operar = int(input())

    if operar == 2:
        print("Muchas gracias")

    elif operar == 1:
        print("ingresar usuario:")
        usuario = input()
        print("ingrese clave")
        clave = int(input())

        if usuario == "pedro" and clave == 6569:
            login = True
            print("bienvenido", usuario, "!")
        elif usuario == "Santiago" and clave == 1313:
             login = True 
             print("Bienvenido", usuario, "1")
        elif usuario == "Juan" and clave == 1234: 
            login = True 
            print("Bienvenido", usuario, "1") 

        else:  
             print("Usuario o clave no válida!") 
        
    else:
             print("Opción No Válida")

    saldo = 2000
    print("Tu saldo inicial es: ", saldo)

    print("---------MENU---------")
    print("Bienvenido a tu cajero automatico")
    print("1. transferencia de fondos")
    print("2. retirar dinero de la cuenta")
    print("3. depositar a otra cuenta")
    print("4. mostrar estado de cuenta")
    print("4. salir")

    opcion = int(input("elija una opcion! "))

    if opcion ==1:
         cantidad = float(input("ingrese el usuario a transferir"))
         #OPERADORES DE ASIGNACION
         saldo== cantidad #saldo = saldo = cantidad que ingresamos
         print("transferencia realizado correctamente, tu saldo actual es: ", saldo)

    if opcion ==2:
         cantidad = float(input("ingrese la cantidad a retirar"))
         #OPERADORES DE ASIGNACION
         saldo== cantidad #saldo = saldo = cantidad que ingresamos
         print("retiro realizado correctamente, tu saldo actual es: ", saldo)

    if opcion ==3:
         cantidad = float(input("ingrese la cantidad a depositar"))
         #OPERADORES DE ASIGNACION
         saldo== cantidad #saldo = saldo = cantidad que ingresamos
         print("deposito realizado correctamente, tu saldo actual es: ", saldo)

    if opcion ==4:
         cantidad = float(input("mostrar estado de cuenta"))
         #OPERADORES DE ASIGNACION
         saldo== cantidad #saldo = saldo = cantidad que ingresamos
         print(" realizado correctamente, tu saldo actual es: ", saldo)      

    elif opcion >= 4 or opcion < 0:
         print("gracias por utilizar nuestros servicios")            