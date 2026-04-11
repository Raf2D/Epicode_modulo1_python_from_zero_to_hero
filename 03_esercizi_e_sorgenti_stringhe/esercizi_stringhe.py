#Esercizio 1: chiedi una frase e inverti l'ordine delle parole

frase = input("Digita una frase: ")
print("Ecco la frase che hai digitato: ", frase)

frase_invertita = frase[::-1]
print("Ecco la frase invertita: ", frase_invertita)

#Esercizio 2: controlla se la frase è un palindromo (ignora spazi e maiusole)

if (frase.upper().strip() == frase_invertita.upper().strip()):
    print("La frase è palindroma")
else:
    print("la frase non è palindroma")