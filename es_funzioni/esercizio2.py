# esericizio 1

#print(f"{"="*3} QUIZ PYTHON {"="*3}")
#print("""Domanda: Qual è il tuo linguaggio di programmazione preferito?\n1. Python\n2. Javascript\n3. Java\n4. C++""")
#risposta = int(input("Inserisci la tua scelta: "))

"""if risposta == 1:
	print("Hai scelto: Python\nOttima scelta! Perché lo useremo per i prossimi quattro mesi!")
elif risposta == 2:
	print("Hai scelto Javascript!")
elif risposta == 3:
	print("Hai scelto Java")
elif risposta == 4:
	print("Hai scelto C++")
else:
	print("devi scegliere un numero tra 1 e 4!")
"""


# esercizio 1 con funzioni

def mostra_menu():
	print(f"""{"="*3} QUIZ PYTHON {"="*3}\nDomanda: Qual è il tuo linguaggio di programmazione preferito?\n1. Python\n2. Javascript\n3. Java\n4. C++""")
mostra_menu()

def raccogli_risposta():
	risposta = int(input("Inserisci la tua scelta: "))
	return risposta
print(raccogli_risposta())

def valida_scelta(scelta):
	if scelta >= 1 and scelta <= 4:
		return True
	else:
		return False

scelta = raccogli_risposta()
print(valida_scelta(scelta))

def genera_feedback(scelta):
	if scelta == 1:
		return "Hai scelto: Python\nOttima scelta! Perché lo useremo per i prossimi quattro mesi!"
	elif scelta == 2:
		return "Hai scelto Javascript!"
	elif scelta == 3:
		return "Hai scelto Java"
	elif scelta == 4:
		return "Hai scelto C++"
	else:
		return "devi scegliere un numero tra 1 e 4!"
scelta = raccogli_risposta()
print(genera_feedback(scelta))

def mostra_feedback(messaggio):
	print(f"""{"="*3} {messaggio} {"="*3}""")
mostra_feedback("Grazie per aver effettuato il quiz")
