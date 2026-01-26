#Esercizio 1.1: Manipolazione Base
#File: liste_base.py
#Obiettivo: Familiarizzare con i metodi base delle liste.
#
#Consegna:
#Creare una lista server contenente: ["web01", "db01", "cache01"]
#Aggiungere "backup01" alla fine
#Inserire "proxy01" all'inizio (indice 0)
#Rimuovere "cache01"
#Stampare la lista finale e la sua lunghezza
#
#Output Atteso:
#['proxy01', 'web01', 'db01', 'backup01']
#Numero server: 4

server = ["web01", "db01", "cache01"]
server.append("backup01")

server.insert(0,"proxy01")
server.remove("cache01")
print(f"{server}\nNumero server: {len(server)}")



