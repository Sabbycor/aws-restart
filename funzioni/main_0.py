def blocco_1(nome: str) -> None:
    print("=" * 40)
    print(f"    BENVENUTO {nome} NEL SISTEMA")
    print("=" * 40)


def restituisce_divisore(simbolo: str, coefficiente: int):
    print(f"{simbolo}" * coefficiente)


def restituisce_frase_con_divisore(frase: str) -> str:
    return (
        f"{restituisce_divisore('*', 40)} - {frase} - {restituisce_divisore('*', 40)}"
    )


def restituisce_frase_con_nome(nome: str) -> str:
    return f"BENVENUTO {nome} NEL SISTEMA"


risultato_da_stampare = restituisce_frase_con_divisore(
    restituisce_frase_con_nome("anna")
)

print(risultato_da_stampare)
