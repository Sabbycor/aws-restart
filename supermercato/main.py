def get_articolo_formattato(articolo: str) -> str:
    if not articolo:
        print("Prodotto non valido! L'articolo non deve essere vuoto")
    return articolo.lower().strip()

def main():
    print("START DELLA LISTA DELLA SPESA")
    lista_della_spesa:list[str] = []
    lista_carrello:list[str] = []
    
    while True:
        
        articolo = input("Inserisci l'articolo nella lista della spesa: ")
        articolo_formattato: str = get_articolo_formattato(articolo)
        
        if articolo_formattato in lista_della_spesa:
            print("Articolo già inserito")
        else:
                lista_della_spesa.append(articolo_formattato)
        
        continua = input("Vuoi aggiungere altri prodotti? (si/no): ").strip().lower()
        
        if continua != "si":
            break

    print(f"La tua lista: {lista_della_spesa}")
    print("LISTA CONCLUSA")
    
main()