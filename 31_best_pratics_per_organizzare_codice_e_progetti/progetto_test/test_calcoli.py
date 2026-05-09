import unittest
from src.calcoli import calcola_danno

class TestPokemon(unittest.TestCase):

    def test_danno_standard(self):
        #Caso normale: 50 attacco vs 30 difesa = 20 danno
        self.assertEqual(calcola_danno(50,30),20)
    
    def test_difesa_alta(self):
        #Caso difesa superiore: deve restituire 1, non numeri negativi
        self.assertEqual(calcola_danno(10,100),1)

    def test_valore_limite(self):
        #Caso attacco e difesa uguali: deve restituire 1 
        self.assertEqual(calcola_danno(50, 50), 1)

if __name__ == '__main__':
    unittest.main()