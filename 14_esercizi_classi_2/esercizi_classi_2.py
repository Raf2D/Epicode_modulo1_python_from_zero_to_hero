#Esercizio pratico lezione "L'incapsulamento e la Generalizzazione"

#Crea una classe Persona con attributo "nome" e metodo presentati()
#Poi crea una sottoclasse Studente che aggiunge l'attributo "corso" e lo include nella presentazione
#infine, rendi l'attributo nome privato e permetti di leggerlo solo tramite un metodo dedicato

class Persona():

    def __init__(self,nome):
            self.__nome = nome #rendo nome un attributo privato
    
    def presentati(self):
          return f"Ciao sono {self.__nome}"
    
    #metodo getter
    def mostra_nome(self):
          return self.__nome
          

class Studente(Persona): #estende la classe persona
      
      def __init__(self, nome, corso):
           super().__init__(nome)
           self.corso = corso
    
      def presentati(self):
            return super().presentati() + f", frequento il corso di {self.corso}"
      

#-------------------ESECUZIONE DEL PROGRAMMA-------------------------------------------------------------#

st1 = Studente("Luca","Informatica")
print(st1.presentati())
    