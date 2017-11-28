import unittest
import ejercicio2

class ejercicio2_test (unittest.TestCase):

    def testBatallaDeBotesRecibeUnMapaConUnaListaVaciaDeberiaRetornarListaVacia(self):
        #Arrange
        Mapa=[]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        #Act
        resultado= ejercicio2.batallaDeBotes(Mapa,posicionesDeDisparosDePrueba)
        #Assert
        self.assertTrue(resultado == [])

    def testBatallaDeBotesRecibeUnMapaVacioDeberiaRetornarUnaListaVacia(self):
        #Arrange
        Mapa = [""]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        #Act
        resultado= ejercicio2.batallaDeBotes(Mapa,posicionesDeDisparosDePrueba)
        #Assert
        self.assertTrue(resultado == [])

    def testBatallaDeBotesRecibeUnMapaConEspacioVaciosDeberiaRetornarUnaListaVacia(self):
        #Arrenge
        Mapa = ["      "]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.batallaDeBotes(Mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertEqual(resultado,[])

    def testBatallaDeBotesRecibeUnMapaConUnaFraseNoValidaDeberiaRetornarUnaListaVacia(self):
        #Arrange
        Mapa = ["soy NO valido"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.batallaDeBotes(Mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertTrue(resultado == [])

    def testBatallaDeBotesRecibeUnMapaConOtraFraseNoValidaDeberiaRetornarUnaListaVacia(self):
        #Arrenge
        Mapa = ["yo","tambien","soy","invalido"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.batallaDeBotes(Mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertEqual(resultado, [])

    def testBatallaDeBotesRecibeUnMapaConPosicionesDeBarcosSinHundirDeberiaRetornarUnaListaVacia(self):
        #Arrenge
        Mapa = ["b.b.","....","..bb","b.b"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.batallaDeBotes(Mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertTrue(resultado == [])

    def testBatallaDeBotesRecibeUnMapaConPosicionesDeBarcosSinHundirDeberiaRetornarUnaListaConPosicionesDeBarcosHundidos(self):
        #Arrenge
        Mapa = "b.b..","b...b",".....","....b"
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.batallaDeBotes(Mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertEqual(resultado,[(2,1),(2,5)])

    def TestBatallaDeBotesRecibeUnMapaConPosicionesDeBarcosSinHundirUnaListaVaciaDeberiaRetornarUnaListaConPosicionesDeBarcosHundidos(self):
        #Arrenge
        Mapa = ["b..","...","..b"]
        posicionesDeDisparosDePrueba = []
        # Act
        resultado = ejercicio2.batallaDeBotes(Mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertTrue(resultado == [(1,1),(3,3)])
