Persone = {}

size = int(input("Inserisci la grandezza della tabella: "))

for i in range(size):
    dict_name = input("Inserisci una persona: ")

    Persone[dict_name] = {}

    x = Persone[dict_name].get

    Persone[dict_name]['Cognome'] = input("Inserisci il cognome: ")

    Persone[dict_name]['Nome'] = input("Inserisci il nome: ")
    
    Persone[dict_name]['Altezza'] = int(input("Inserisci l'altezza: "))
    if (x('Altezza')) > 230 or (x('Altezza')) < 50:
        print("ATTENZIONE L'ALTEZZA DEV'ESSERE COMPRESA TRA 50CM E 230CM")
        break
        
    Persone[dict_name]['Peso'] = int(input("Inserisci il peso: "))
    if (x('Peso')) > 150 or (x('Peso')) < 10:
        print("ATTENZIONE IL PESO DEV'ESSERE COMPRESO TRA 10KG E 150KG")
        break
        
    Persone[dict_name]['Sesso'] = input("Inserisci il sesso: ")
    if not((x('Sesso')) == "M" or (x('Sesso')) == "F" or (x('Sesso')) == "A"):
        print("IL SESSO DEV'ESSERE COMPRESO TRA M/F O A")
        break

    Persone[dict_name]['Anno di nascita'] = int(input("Inserisci l'anno di nascita: "))
    if (x('Anno di nascita')) > 2022 or (x('Anno di nascita')) < 1900:
        print("L'ANNO DI NASCITA DEV'ESSERE COMPRESO TRA IL 1900 E IL 2022")
        break

for k, v in Persone.items():
    print(k + ": " + str(v))
    break

    


#! Univocità cognome e nome
#! visualizzare cognome, nome e sesso della persona più giovane
#! contare le persone più alte di 200cm e più pesanti di 100kg