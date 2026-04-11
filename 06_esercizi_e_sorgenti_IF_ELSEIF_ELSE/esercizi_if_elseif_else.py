#Esercizio sulla lezione "Condizioni IF, ELSEIF, ELSE"

#Scrivi un programma che :
#ha una variabile eta
#se età < 18 stampa "Sei minorenne"
#se età è almeno 18 ma meno di 65 stampa "Sei adulto"
#altrimenti stampa "Sei anziano"

eta = int(input("Quanti anni hai ?: "))

if(eta < 18):
    print(f"Hai {eta} anni, quindi sei minorenne.")
elif(eta >= 18 and eta < 65):
    print(f"Hai {eta} anni, sei adulto.")
else:
    print(f"Hai {eta} anni, sei anziano.")