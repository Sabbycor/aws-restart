# crea funzioni che utilizzano control flow e return
"""restituisce_numero_pari(numero)
Prende un numero come parametro
Restituisce True se il numero è pari, False se è dispari
Usa l'operatore modulo % e un if/else"""

"""def restituisce_num_pari(numero: int ):
	if numero  % 2 == 0:
		return f"il numero {numero} è pari"
	else:
		return f"il numero {numero} è dispari"

numero = int(input("Inserisci un numero pari:"))
risultato = restituisce_num_pari(numero)
print(risultato)"""


"""calcola_sconto(prezzo, età)
Prende prezzo e età come parametri
Se eta < 18: sconto 20%
Se eta >= 65: sconto 30%
Altrimenti: nessuno sconto
Restituisce il prezzo finale"""

"""def calcola_sconto(prezzo,eta):
	if eta < 18:
		return prezzo - (prezzo * 20 / 100)
	elif eta >= 65:
		return prezzo - (prezzo * 30 / 100)
	else:
		return "nessuno sconto"

eta = int(input("Inserisci la tua età: "))
prezzo = float(input("Inserisci il prezzo: "))
print(f"Prezzo finale: {calcola_sconto(prezzo, eta)} euro")"""


"""valuta_temperatura(gradi)
Prende la temperatura come parametro
Restituisce una stringa:
"Freddo" se < 15
"Mite" se 15-25
"Caldo" se > 25"""


"""def valuta_temperatura(gradi):
	if temperatura < 15:
		return "Freddo"
	elif temperatura >= 15 and temperatura <= 25:
		return "Mite"
	else:
		return "Caldo"
temperatura = float(input("Inserisci la temperatura: "))
risultato = valuta_temperatura(temperatura)
print(risultato)"""


"""Crea le seguenti funzioni che utilizzano control flow e print (senza return)

stampa_tabellina(numero)
Prende un numero come parametro
Usa un ciclo for per stampare la tabellina da 1 a 10
Non restituisce nulla, solo stampa"""

"""def stampa_tabellina(numero):
	for i in range(11):
		print(numero * i)
parametro = int(input("Inserisci un numero: "))
stampa_tabellina(parametro)"""


"""disegna_rettangolo(larghezza, altezza)
Prende larghezza e altezza come parametri
Usa cicli for annidati per stampare un rettangolo di asterischi
Non restituisce nulla, solo stampa"""


def disegna_rettangolo(larghezza):
	for i in range(10):
		print(i)

larghezza = input("inserisci la larghezza: ")
disegna_rettangolo(larghezza)
