import unittest
import ejercicio1

class ejercicio1_test (unittest.TestCase):

    def testRotacionesDePalabraRecibeCadenaVaciaRetornaListaVacia(self):
        #Arrenge
        cadena = ""
        #Act
        resultado = ejercicio1.rotacionesDePalabra(cadena)
        #Assert
        self.assertttue(resultado)