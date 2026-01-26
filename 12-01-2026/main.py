"""class Formina:
    #qui entra in gioco il costruttore, una funzione che entra in gioco ogni volta che voglio creare un biscotto
    def __init__(self, nome_forma: str):
        self.forma = nome_forma

# Creazione del biscotto
biscotto1 = Formina("cuoricino")
biscotto2 = Formina("stellina")

print(biscotto1.forma)
print(biscotto2.forma)

"""
class Persona:
    def __init__(self, nome: str, cognome: str, isEdgemonyPartecipant: bool):
        self.nome = nome
        self.cognome = cognome
        self.isEdgemonyPartecipant = isEdgemonyPartecipant
    
    def print_nome(self) -> None:
        print(self.nome)
    
    def printIsEdgemonyPartecipant(self) -> None:
        print(f"{self.nome} {self.cognome}: {self.isEdgemonyPartecipant}")

class Corso:
    def __init__(self, nome: str):
        self.nome = nome
        self.partecipanti = []
        
    def addPartecipanti(self, p: Persona) -> bool:
        if p.isEdgemonyPartecipant:
            self.partecipanti.append(f"{p.nome} {p.cognome}")
            return True
        
        else:
            return False
        
persona1 = Persona("sabrina", "corrado", True)
persona2 = Persona("Valeria", "Anjoi", True)
persona3 = Persona("Maria", "rossi", False)

corso1 = Corso("Edgemony")

partecipanti_list = [persona1, persona2, persona3]

for p in partecipanti_list:
    print(f"Prima: {corso1.partecipanti}")
    print(corso1.addPartecipanti(p))
    print(f"Dopo: {corso1.partecipanti}")


