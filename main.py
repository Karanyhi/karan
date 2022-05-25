import random
import platform
import requests
import subprocess
import time
from googlesearch import search
from colorama import *

init(autoreset=True) #Inicia la función init de colorama y se resetea cada vez que se llama la función
print(Fore.LIGHTWHITE_EX+"\n          [Created by Karanyhi]")
print(Fore.LIGHTWHITE_EX+"            IG: "+Fore.LIGHTGREEN_EX+"@K4ranyhi")

if platform.system().lower()=='windows': #Detecta sistema operativo
	param='-n'
	print(Fore.LIGHTWHITE_EX+"\n [S.O] Windows detected.")
else:
	param='-c'
	print(Fore.LIGHTWHITE_EX+"\n [S.O] Linux detected.")


print("  _   __   ___                             _                                 _")
print(" | | / /  /   |                           | |                               | |")
print(" | |/ /  / /| | _ __   __ _  _ __         | |      __ _  _   _  _ __    ___ | |__    ___  _ __")
print(" |    \ / /_| || '__| / _` || '_ \        | |     / _` || | | || '_ \  / __|| '_ \  / _ \| '__|")
print(" | |\  \\___   || |   | (_| || | | |       | |____| (_| || |_| || | | || (__ | | | ||  __/| |")
print(" \_| \_/    |_/|_|    \__,_||_| |_|       \_____/ \__,_| \__,_||_| |_| \___||_| |_| \___||_|")


while(True):#While general
    while(True): #Pregunta y valida opciones
        try:
            print(Fore.WHITE + "\n[" +Fore.GREEN+ "+" +Fore.WHITE+"]"+Fore.LIGHTYELLOW_EX+" Ingrese una de las opciones: ")
            print(Fore.WHITE + "\n [" +Fore.RED+ "1" +Fore.WHITE+"]"+Fore.CYAN+" Ping (Domain or IP).")
            print(Fore.WHITE + " [" +Fore.RED+ "2" +Fore.WHITE+"]"+Fore.CYAN+" WebScraping.")
            print(Fore.WHITE + " [" +Fore.RED+ "3" +Fore.WHITE+"]"+Fore.CYAN+" Geolocalización.")
            print(Fore.WHITE + " [" +Fore.RED+ "4" +Fore.WHITE+"]"+Fore.CYAN+" Exit.")
            op=int(input("\n Opción: "))
            if op<=4 and op>=1:
                break
            else:
                print(Fore.RED+" ERR: Ingrese una opción Válida (1 to 4)")
        except ValueError:
            print(Fore.RED+" ERR: Ingrese un número válido")
#-------------------------------------------------------------------------------------
    if (op==1):#Opción 1 (Pide IP y envía un paquete a través de la powershell)
        ip=input(" \nIngrese IP: ")
        
        comando='ping '+param+' 2 '+ip
        response=subprocess.call(comando)
        if (response == 0):
             print(Fore.WHITE + "\n [" +Fore.GREEN+ "+" +Fore.WHITE+"]"+Fore.GREEN+" Ejecutado con éxito!!!")
        else:
             print(Fore.WHITE + "\n [" +Fore.LIGHTRED_EX+ "!" +Fore.WHITE+"]"+Fore.RED+" ERR: IP no válida")  

    if (op==2): #Opción 2
        term=input(" \n Introduzca un término de busqueda: ")
        while(True):#Valida cant de resultados
            try:
                nms=int(input(" \n Introduzca la cantidad de resultados: "))
                if nms>=1:
                    break
                else:
                    print(Fore.RED+" \nERR: introduzca una cantidad válida")
            except ValueError:
                print(Fore.RED+"\nERR: Introduzca sólo números enteros")

        print("\n")
        for i in search(term, num_results=nms, lang='es'): 
            print(Fore.GREEN+i)
        print(Fore.WHITE)
    if (op==3):
        ipgeo=input(" \nIngrese IP:")
        respuesta=requests.get("http://ip-api.com/json/"+ipgeo).json()

        print(" IP: "+respuesta['query'])
        if respuesta["status"]== str("success"):
            print(respuesta['status'])
            print(respuesta['country'])
            print(respuesta['countryCode'])
            print(respuesta['region'])
            print(respuesta['regionName'])
            print(respuesta['city'])
            print(respuesta['zip'])
            print(respuesta['lat'])
            print(respuesta['lon'])
            print(respuesta['timezone'])
            print(respuesta['isp'])
            print(respuesta['org'])
            print(respuesta['as'])
        else:
            print(Fore.RED+"\n ERR: IP inexistente o no encontrada")
    if (op==4):
        print(Fore.LIGHTGREEN_EX+" \n GoodBye!")
        exit()

    while(True):#Pregunta término o continuación del programa
        resp=input(" \n Desea volver al menú de opciones? S/N: ").upper()
        if resp=="S" or resp=="N":
            break
        else:
            print(Fore.RED+" \nERR: Ingrese solo S/N")
    if resp=="N":
        print(Fore.LIGHTGREEN_EX+" \n GoodBye!")
        break
    else:
        continue 


