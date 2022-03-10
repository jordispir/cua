import datetime
import os

#[nom, tlf, time(year, day, hour, minute)]

realTime = datetime.datetime.now()

year = realTime.year
day = realTime.day
hour = realTime.hour
minute = realTime.minute
second = realTime.second


cuaEspera = []
cuaAtessos = []

def atendreClient(cuaEspera, cuaAtessos):
    client = cuaEspera[0]
    
    cuaAtessos.append(client)
    cuaEspera.remove(client)

    input("El client ha sigut ates... enter")

def afegirClient(cuaEspera):
    nouClient, tlf = input("Nom del client, telefon: ").split()
    cuaEspera.append([nouClient, tlf, ("Hora entrada: " + str(hour) + ":" + str(minute) + ":" + str(second) ) ] )
    
    input("continuar? pressionar enter...")

opcio = None
while(opcio != "4"):

    print("Gestio de clients")
    print("1. Llistar cua")
    print("2. Afegir client a la cua de espera") #afegir a l'hora real.
    print("3. Atendre client")
    print("4. sortir")
    opcio = input("Indica la entrada: ")

    if opcio == "1":
        os.system('cls')
        print("Cua Espera")
        print("==========")

        for c in cuaEspera:
            print(c)


        print("\nCua Atessos")
        print("==========")

        for c in cuaAtessos:
            print(c)

        input("continuar? pressionar enter...")

    elif opcio == "2":
        afegirClient(cuaEspera)

    elif opcio == "3":
        atendreClient(cuaEspera, cuaAtessos)

    os.system('cls')

#guardar hora segons cronologia.