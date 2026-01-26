#Esercizio 2.1: Creazione e Accesso
#File: dizionari_base.py
#Obiettivo: Creare dizionari e accedere ai valori.
#Consegna:
#Creare un dizionario config con le seguenti coppie:
#"host": "192.168.1.1"
#"port": 8080
#"ssl": True
#"timeout": 30
#Stampare il valore di "host"
#Modificare "port" in 443
#Aggiungere una nuova chiave "protocol" con valore "https"
#Stampare il dizionario completo
#
#Output Atteso:
#Host: 192.168.1.1
#{'host': '192.168.1.1', 'port': 443, 'ssl': True, 'timeout': 30, 'protocol': 'https'}

config = {"host": "192.168.1.1", "port": 8080, "ssl": True, "timeout": 30}
print(config["host"])

#per fare modifiche ai valori di una chiave
#metodo 1
config.update({"port": 443})
print(config)
#metodo 2
config["port"] = 443
print(config)

#AGGIUNGERE CHIAVE
config["protocol"] = "https"

print(config)



