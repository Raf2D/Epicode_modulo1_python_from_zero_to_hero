"""
funzione che calcola il danno di un attacco. Invece di usare input(), passeremo
i dati come argomenti, che è il modo migliore per scrivere codice testabile.
"""

def calcola_danno(attacco, difesa):
    """Calcola il danno: (Attacco - Difesa). Se la difesa è più alta, il danno è 1"""
    danno = attacco - difesa
    return danno if danno > 0 else 1