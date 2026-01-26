#Esercizio 1.3: Ordinamento e Ricerca
#File: ordinamento.py
#Obiettivo: Ordinare liste e verificare esistenza elementi.
#Consegna:
#Creare una lista prezzi contenente: [45.5, 12.0, 78.3, 23.1, 56.7]
#Creare una copia ordinata della lista (usando sorted())
#Trovare il prezzo minimo e massimo
#Verificare se 23.1 è nella lista
#Contare quanti prezzi sono maggiori di 50
#
#Output Atteso:
#Prezzi originali: [45.5, 12.0, 78.3, 23.1, 56.7]
#Prezzi ordinati: [12.0, 23.1, 45.5, 56.7, 78.3]
#Minimo: 12.0
#Massimo: 78.3
#23.1 presente: True
#Prezzi > 50: 2

prezzi = [45.5, 12.0, 78.3, 23.1, 56.7]

print(sorted(prezzi))
#OPPURE:
#prezzi.sort()
#print(prezzi)

print(f"Il prezzo massimo è: {max(prezzi)}\nIl prezzo minimo è: {min(prezzi)}")

if 47.6 in prezzi:
    print(True)
else:
    print(False)
    
#print(23.1 in prezzi)


prezzi_maggiori = 0

for x in prezzi:
    if x > 50:
        prezzi_maggiori += 1
    else:
        None
print(prezzi_maggiori)

# OPPURE
# sum(1 for p in prezzi if p > 50)