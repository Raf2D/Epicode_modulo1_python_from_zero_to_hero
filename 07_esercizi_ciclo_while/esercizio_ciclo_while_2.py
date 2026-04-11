#Esercizio lezione "Esercizi Ciclo While"

#Calcolare la somma delle cifre di un numero

numero = int(input("Inserisci un numero intero: "))

numero_string = str(numero)
somma = 0
i = 0

while i < len(numero_string) :
    somma += int(numero_string[i])
    i += 1

print("Ecco la somma delle cifre del numero inserito: ", somma)