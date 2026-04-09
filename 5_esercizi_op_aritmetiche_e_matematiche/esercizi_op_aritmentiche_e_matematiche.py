#Esercizio lezione "operazioni aritmetiche e matematiche": 

# chiede all'utente quanti euro ha
# chiede il prezzo di un singolo oggetto
# usa // per calcolare quante unità può comprare
# usa % per calcolare quanti euro restano


soldi_utente = float(input("Quanti soldi hai a disposizione ? :"))

prezzo_caduno = float(input("Quale è il prezzo di un singolo prodotto ? :"))

quantita_acquistabili = soldi_utente // prezzo_caduno

soldi_utente_restanti = soldi_utente % prezzo_caduno

print(f"Con {soldi_utente} euro puoi comprare {int(quantita_acquistabili)} prodotti e restano {soldi_utente_restanti} euro.")