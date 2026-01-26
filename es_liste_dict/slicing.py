#Esercizio 1.2: Slicing e Accesso
#File: slicing.py
#Obiettivo: Praticare l'accesso agli elementi e lo slicing.
#Consegna:
#Creare una lista temperature contenente: [15, 18, 22, 25, 28, 30, 27, 24, 20]
#Stampare la prima temperatura
#Stampare l'ultima temperatura
#Stampare le temperature dalla posizione 2 alla 5 (esclusa)
#Stampare tutte le temperature con step 2 (saltando una ogni due)
#
#Output Atteso:
#Prima temperatura: 15
#Ultima temperatura: 20
#Temperature [2:5]: [22, 25, 28]
#Ogni due: [15, 22, 28, 27, 20]

temperatura = [15, 18, 22, 25, 28, 30, 27, 24, 20]
print(temperatura[0])
print(temperatura[-1])
print(temperatura[2:5])
print(temperatura[::2]) #lista[inizio:fine:step], così gli dico da inizio a fine direttamente, senza dover specificare
