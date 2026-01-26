import sys
import psutil

#def menu():
#	print(f"""{'-'*5} SYSTEM MONITOR INTERATTIVO {'-'*5}\n1. Versione Python\n2. Piattaforma sistema operativo\n3. Memoria RAM totale (in bytes)\n4. Memoria RAM disponibile (in bytes)\n5. Percentuale utilizzo CPU\n6. Numero di CPU logiche""")
#menu()
#
#def seleziona():
#	if scelta == 1:
#		return f"""{'-'*3} RAM TOTALE {'-'*3}\n Valore:\n{sys.version}"""
#	elif scelta == 2:
#		return f"""{'-'*3} SISTEMA OPERATIVO {'-'*3}\n Valore:\n{psutil.virtual_memory().total}"""
#	elif scelta == 3:
#		return f"""{'-'*3} RAM TOTALE {'-'*3}\nValore:\n{psutil.virtual_memory().total}"""
#	elif scelta == 4:
#		return f"""{'-'*3} RAM DISPONIBILE {'-'*3}\nValore:\n{psutil.virtual_memory().available}"""
#	elif scelta == 5:
#		return f"""{'-'*3} UTILIZZO CPU {'-'*3}\nValore:\n{psutil.cpu_count()}"""
#	elif scelta == 6:
#		return f"""{'-'*3} NUMERO CPU {'-'*3}\nValore:\n{psutil.disk_usage('/').total}"""
#	else:
#		return "Opzione non valida. Scegli un numero tra 1 e 6"
#
#
#scelta = int(input("Inserisci la tua scelta: "))
#print(seleziona())


def menu_completo():
    while True:
        print(f"""{'-'*5} SYSTEM MONITOR INTERATTIVO {'-'*5}
1. Versione Python
2. Piattaforma sistema operativo
3. Memoria RAM totale (in bytes)
4. Memoria RAM disponibile (in bytes)
5. Percentuale utilizzo CPU
6. Numero di CPU logiche
0. Esci
""")
        
        scelta = int(input("Inserisci la tua scelta: "))
        
        if scelta == 0:
            print("Uscita dal programma...")
            break
        elif scelta == 1:
            print(f"""{'-'*3} VERSIONE PYTHON {'-'*3}
Valore:
{sys.version}
""")
        elif scelta == 2:
            print(f"""{'-'*3} SISTEMA OPERATIVO {'-'*3}
Valore:
{platform.system()} {platform.release()}
""")
        elif scelta == 3:
            print(f"""{'-'*3} RAM TOTALE {'-'*3}
Valore:
{psutil.virtual_memory().total} bytes
""")
        elif scelta == 4:
            print(f"""{'-'*3} RAM DISPONIBILE {'-'*3}
Valore:
{psutil.virtual_memory().available} bytes
""")
        elif scelta == 5:
            print(f"""{'-'*3} UTILIZZO CPU {'-'*3}
Valore:
{psutil.cpu_percent(interval=1)}%
""")
        elif scelta == 6:
            print(f"""{'-'*3} NUMERO CPU LOGICHE {'-'*3}
Valore:
{psutil.cpu_count(logical=True)}
""")
        else:
            print("Opzione non valida. Scegli un numero tra 0 e 6\n")

menu_completo()