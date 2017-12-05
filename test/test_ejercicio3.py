import unittest
import ejercicio3

class ejercicio3_test (unittest.TestCase):

    def testGanadorDeLigaRecibeUnaListaDeEquiposVaciaDeberiaRetornarUnaCadenaVacia(self):
        #Arrenge
        equipos = []
        #Act
        resultado = ejercicio3.ganadorDeLiga(equipos)
        #Assert
        self.assertEqual(resultado,"")

    def testGandorDeLigaRecibeUnaListaDeTuplasConEquiposDeberiaRetornasUnaCadenaConElEquipoGanador(self):
        #Arrenge
        equipos = [("a", 1, "b", 0)]
        #Act
        resultado = ejercicio3.ganadorDeLiga(equipos)
        #Assert
        self.assertEqual(resultado, "a")

    def testGanadorDeLigaRecibeUnaListaConTresPartidosDeberiaRetornarElEquipoGanador(self):
        # Arrenge
        equipos = [("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]
        # Act
        resultado = ejercicio3.ganadorDeLiga(equipos)
        # Assert
        self.assertEqual(resultado,"c")

    def testGanadorDeLigaRecibeUnaListaDeTuplasConTresPartidosDeberiaRetornarElEquipoGanadorEnOrdenAlfabetico(self):
        # Arrenge
        equipos = [("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]
        # Act
        resultado = ejercicio3.ganadorDeLiga(equipos)
        # Assert
        self.assertEqual(resultado, "Almagro")

    def testGanadorDeLigaRecibeUnaListaDeTuplasConCuatroPartidosDeberiaRettornarElEquipoGanador(self):
        # Arrenge
        equipos = [("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]
        # Act
        resultado = ejercicio3.ganadorDeLiga(equipos)
        # Assert
        self.assertTrue(resultado == "a")
