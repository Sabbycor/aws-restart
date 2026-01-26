#start
def is_lista_utente_filled(lista_utente: list[str]) -> bool:
    if len(lista_utente) < 3:
        return True
    else:
        return False

def get_ingrediente_formattato(ingrediente: str) -> str:
    if not ingrediente:
        print("L'ingrediente non deve essere vuoto")
    return ingrediente.lower().strip()

def get_input_from_utente(text: str) -> str:
    print("*"*30)
    if not text:
        print("il messaggio non deve essere vuoto")
    return input(text)

def log_message(text:str, type):
    icon = None
    match type:
        case "ALERT":    
            icon = "⚠️"
        case "INFO":
            icon = "ℹ️"
    print(f"{icon} - {text}")
    


def main() -> None:
    log_message("Start del programma", "INFO")

    lista_ricetta: list[str] = ["farina", "acqua", "lievito"]

    lista_utente: list[str] = []
    
    while is_lista_utente_filled(lista_utente): # se non si specifica nulla è == True
        ingrediente = get_input_from_utente("Inserisci un ingrediente: ")
        if not ingrediente:
            log_message("L'ingrediente non deve essere vuoto", "ALERT")
        
        ingrediente_formattato: str = get_ingrediente_formattato(ingrediente)
        
        if ingrediente_formattato in lista_ricetta:
            #print("Ingrediente nella ricetta")
            if ingrediente_formattato in lista_utente:
                print("Ingrediente già inserito")
            else:
                lista_utente.append(ingrediente_formattato)
                print(lista_utente)
        else:
            log_message("Ingrediente non valido", "ALERT")

    print("Impasta e fai la pizza")
    print("End del programma")

    
main()