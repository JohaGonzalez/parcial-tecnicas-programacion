import unittest
import ejercicio1

class ejercicio1_test (unittest.TestCase):

    def testRotacionesDePalabraRecibeCadenaVaciaDeberiaRetornarListaVacia(self):
        #Arrenge
        cadena = ""
        #Act
        resultado = ejercicio1.rotacionesDePalabra(cadena)
        #Assert
        self.assertEqual(resultado,[])

    def TestRotacionesDePalabraRecibeCadenaVaciaConEspacioDeberiaRetornarListaVacia(self):
        #Arrenge
        cadena = "     "
        #Act
        resultado = ejercicio1.rotacionesDePalabra(cadena)
        #Assert
        self.assertEqual(resultado,[])

    def testRotacionesDePalabraRecibeCadenaConUnCaracterDeberiaRetornarListaConElMismoCaracter(self):
        #Arrenge
        cadena = "a"
        #Act
        resultado = ejercicio1.rotacionesDePalabra(cadena)
        #Assert
        self.assertTrue(resultado == ['a'])

    def testRotacionesDePalabraRecibeUnaCadenaConDosCaracteresDeberiaRetorarListaConRotacionDeCaracteres(self):
        #Arrenge
        cadena = "ab"
        #Act
        resultado = ejercicio1.rotacionesDePalabra(cadena)
        #Assert
        self.assertTrue(resultado ==['ab','ba'])

    def testRotacionesDePalabraRecibeUnaCadenaConUnaPalabraDeberiaRetornarUnaListaConLaRotacionDeLaPalabra(self):
        #Arrenge
        cadena = "paz"
        #Act
        resultado = ejercicio1.rotacionesDePalabra(cadena)
        #Assert
        self.assertEqual(resultado,['paz','azp','zpa'])

    def testRotacionesDePalabraRecibeUnaCadenaConUnaPalabraDivididaDeberiaRetornarUnaListaConLaRotacionDeLaPalabra(self):
        #Arrenge
        cadena = "so l"
        #Act
        resultado = ejercicio1.rotacionesDePalabra(cadena)
        # Assert
        self.assertTrue(resultado == ['so l','o ls',' lso','lso '])

    def testRotacionesDePalabraRecibeUnaCadenaConOtraPalabraDeberiaRertornarUnalistaConLasRotacionesDeEsasPalabras(self):
        #Arrange
        cadena = "rotar"
        #Act
        resultado = ejercicio1.rotacionesDePalabra(cadena)
        # Assert
        self.assertEqual(resultado,['rotar','otarr','tarro','arrot','rrota'])



