#-----ESERCIZIO 1--------------------------------------------------------------------------------#

#Scrivi un programma che chieda all'utente la sua età e se ha la patente (si / no).

#Il programma deve stampare True se la persona può guidare (età maggiore o uguale a 18 e ha la patente).

#Deve stampare False in tutti gli altri casi.

eta = int(input("Inserisci la tua età: "))
patente = input("Hai la patente ? : ")


if(eta >= 18 and patente.upper() == 'SI'):
    print(True)
elif(eta < 18 and patente.upper() == 'SI'):
    print("Impossibile, non puoi avere la patente perchè hai una età inferiore a 18 anni. ", False)
else:
    print(False)


#-----ESERCIZIO 2-------------------------------------------------------------------------------#

#Un utente può entrare in biblioteca se:

#non è in ritardo con la restituzione di libri oppure

#ha un abbonamento premium.

#Scrivi un programma che, date due variabili booleane (ritardo e premium), stampi True se l'utente può entrare, altrimenti False.

orario_arrivo = float(input("A che ora è entrato l'utente in biblioteca ? :"))

max_orario_entrata = 9.30

if (max_orario_entrata < orario_arrivo):
    print("L'utente può entrare ?", False)
else:
    print("L'utente non può entrare ?", True)