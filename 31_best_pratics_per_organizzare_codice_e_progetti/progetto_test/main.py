from src.calcoli import calcola_danno

def start_game():
    print("--- Simulazione di Lotta Pokemon ---")

    try:
        att = int(input("Inserisci i punti Attacco del tuo Pokemon: "))
        dif = int(input("Inserisci i punti Difesa del Pokemon avversario: "))

        #usiamo la funzione che abbiamo già testato con successo
        risultato = calcola_danno(att, dif)

        print(f"\nIl danno inflitto è di {risultato} HP !")
    except ValueError:
        print("Errore: devi inserire dei numeri interi!")


if __name__ == "__main__":
    start_game()