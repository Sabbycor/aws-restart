# Funzioni
# racchiudere in uno spazio di memoria il blocco del codice.
# def sta per define, è un blocco di istruzioni

def blocco1(nome : str) -> None:
	print("="*40)
	print("Benvenuto {nome} nel sistema")
	print("="*40)

blocco1(nome)

nome = str(input("inserisci il tuo nome: "))
def saluta(nome):
	print(f"ciao {nome}\nBenvenuto nel sistema")

saluta(nome)

def blocco_2(nome: str) -> str:
	return f"BENVENUTO {nome} NEL SISTEMA"

print(blocco_2("anna"))

def stampa_frase_con_divisore(frase: str) -> str:
	divisore: str = "="*40
	return f"{divisore}\n{nome}\n{divisore}"

frase : str = blocco_2("sab")
risultato = stampa_frase_con_divisore(frase)
