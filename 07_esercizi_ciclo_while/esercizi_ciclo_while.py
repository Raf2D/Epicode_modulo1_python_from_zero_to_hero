#Esercizio lezione "Ciclo While"

#Prova a scrivere un programma utilizzando il ciclo while che:
#chiede all'utente di inserire un numero positivo.
#continua a chiedere finchè l'utente non inserisce un numero positivo (>0)
#quando il numero è positivo, stampa "Hai inserito il numero positivo: X" e termina

numero = 0

while numero <= 0 :

    numero = float(input("Inserisci un numero positivo: "))

    if numero > 0 : 
        print("Hai inserito il numero positivo maggiore di 0: ", numero)


