#Esercizio 2.2: Iterazione
#File: iterazione.py
#Obiettivo: Iterare su dizionari.
#Consegna:
#Creare un dizionario utenti con le seguenti coppie:
#"alice": "admin"
#"bob": "user"
#"charlie": "guest"
#Iterare sul dizionario e stampare ogni coppia nel formato: "Username: alice, Ruolo: admin"
#Verificare se "bob" è una chiave presente
#Stampare tutte le chiavi (usernames)
#Stampare tutti i valori (ruoli)
#
#Output Atteso:
#Username: alice, Ruolo: admin
#Username: bob, Ruolo: user
#Username: charlie, Ruolo: guest
#bob presente: True
#Usernames: dict_keys(['alice', 'bob', 'charlie'])
#Ruoli: dict_values(['admin', 'user', 'guest'])

utenti = {"alice" : "admin", "bob": "user", "charlie":"guest"}


for chiave, valore in utenti.items():
    print(f"{'Username'} : {chiave}, {'Ruolo'} : {valore}")
    
if "bob" in utenti:
    print(True)
else:
    print("False")
    
print(utenti.keys())
print(utenti.values())