# control flow

a: int = 2
b: int = a

print(type(a == b))  

"""
# Pippo vuole guidare l'auto, ma può farlo?

# se pippo ha la pantete, puo' guidare
# se pippo non  ha la pantete, non puo' guidare

answer: str = input("Ha la patente?")

if  answer.lower() == "yes": 
    print("puo guidare")
elif answer.lower() == "no":
    print("non puo guidare")
else:
    print("inserisci solo Yes o No") 
"""

piove: bool  = False 
if not piove: 
    print("E' vero, non priove")

answer = input("Quanti anni ha Pippo?")

if answer.isdigit():
    result = "Puo guidare" if int(answer) >= 18 else "Non puo guidare"
    print(result)
else: 
    print("inserisci un valore numerico")
