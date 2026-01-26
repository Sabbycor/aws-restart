#Esercizio 3.1:
#Lista di Dizionari
#File: lista_dizionari.py
#Obiettivo: Gestire una lista di dizionari (simile a un database).
#Consegna:
#Creare una lista prodotti contenente 4 dizionari, ognuno con chiavi "nome", "prezzo", "quantita":
#{"nome": "Laptop", "prezzo": 899.99, "quantita": 5}
#{"nome": "Mouse", "prezzo": 25.50, "quantita": 50}
#{"nome": "Tastiera", "prezzo": 75.00, "quantita": 30}
#{"nome": "Monitor", "prezzo": 299.99, "quantita": 15}
#Iterare sulla lista e stampare solo i prodotti con prezzo superiore a 100
#Calcolare il valore totale dell'inventario (prezzo × quantità per ogni prodotto)
#
#Output Atteso:
#Prodotti > 100€:
#- Laptop: €899.99
#- Monitor: €299.99
#
#Valore totale inventario: €11224.20

prodotti = [
    {"nome": "Laptop", "prezzo": 899.99, "quantita": 5},
    {"nome": "Mouse", "prezzo": 25.50, "quantita": 50},
    {"nome": "Tastiera", "prezzo": 75.00, "quantita": 30},
    {"nome": "Monitor", "prezzo": 299.99, "quantita": 15}
]

inventario: float = 0

#for prodotto in prodotti:
#  inventario += prodotto["prezzo"] * prodotto["quantita"] 
#  print(prodotto["prezzo"]) if prodotto["prezzo"] > 100 else None
#
#print(inventario)

for prodotto in prodotti:
    inventario += prodotto["prezzo"] * prodotto["quantita"]
    if prodotto["prezzo"] > 100:
        print(prodotto["prezzo"])
    else:
        None

print(inventario)

    
