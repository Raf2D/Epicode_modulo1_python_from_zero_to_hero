#Esercizio della lezione sui Set:

#Immaginiamo due corsi universitari: Corso A e Corso B
#vogliamo sapere:
#chi frequenta entrambi i corsi
#chi frequenta solo il corso A
#chi frequenta solo il corso B
#chi frequenta almeno un corso
#quanti studenti unici ci sono in totale



corso_A = {"Alessandro","Federica","Giuseppe","Alessio","Daniele","Rosalba","Rossana"}
corso_B = {"Federica","Alessio","Daniele","Franco","Francesco","Raffaele","Alessia","Giuseppe"}

print("Studenti che frequentano sia il corso A che il corso B: ", corso_A&corso_B) #chi frequenta entrambi i corsi
print("Studenti che frequentano solo il corso A : ", corso_A.difference(corso_B)) #chi frequenta solo il corso A
print("Studenti che frequentano solo il corso B : ", corso_B.difference(corso_A)) #chi frequenta solo il corso B

studenti_iscritti = set()

#Essendo un set non ci saranno ripetizioni di nome
studenti_iscritti.update(corso_A)
studenti_iscritti.update(corso_B)

print("Studenti che frequentano almeno un corso : ", studenti_iscritti) #chi frequenta almeno un corso
print(f"Quindi ho un totale di {len(studenti_iscritti)} studenti iscritti.") #quanti studenti unici ci sono in totale

