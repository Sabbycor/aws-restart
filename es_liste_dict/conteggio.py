#Esercizio 2.3: Conteggio Occorrenze
#File: conteggio.py
#Obiettivo: Usare dizionari per contare occorrenze.
#Consegna:
#Creare una lista voti contenente: ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]
#Creare un dizionario vuoto conteggio
#Iterare sulla lista voti e contare quante volte appare ogni voto nel dizionario
#Stampare il dizionario finale
#Suggerimento: Usare conteggio.get(voto, 0) per gestire chiavi mancanti.
#
#Output Atteso:
#Conteggio voti: {'A': 4, 'B': 3, 'C': 2, 'D': 1}

import collections
voti = ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]

print(collections.Counter(voti))



