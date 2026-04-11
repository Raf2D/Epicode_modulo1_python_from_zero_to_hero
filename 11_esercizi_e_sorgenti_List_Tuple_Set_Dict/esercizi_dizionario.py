#Esercizio della lezione "I dizionari"

#Crea un dizionario che rappresenti uno studente con le seguenti chiavi: "nome","età","corso"
#modifica il valore età
#aggiungi una nuova chiave
#usa get() per recuperare un valore sconosciuto senza errore
#itera su tutte le coppie chiave-valore e stampale



dizionario = {"nome":"Giovanni","età":26, "corso":"informatica"}

print(dizionario["nome"])

dizionario["nome"] = "Roberto"

print(dizionario["nome"])

print("Cerco cognome: ", dizionario.get("cognome","Non trovato"))

#Itero il dizionario
print("#----------Itero il dizionario:")
for chiave, valore in dizionario.items():
    print(f"{chiave}: {valore}")




