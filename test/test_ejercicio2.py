import unittest
import ejercicio2

class ejercicio2_test (unittest.TestCase):

    def testBatallaDeBotesRecibeUnMapaVacioDeberiaRetornarListaVacia(self):
        #Arrange
        mapa=[]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        #Act
        resultado= ejercicio2.batallaDeBotes(mapa,posicionesDeDisparosDePrueba)
        #Assert
        self.assertTrue(resultado == [])

    def testBatallaDeBotesRecibeUnMapaVacioDeberiaRetornarUnaListaVacia(self):
        #Arrange
        mapa = [""]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        #Act
        resultado= ejercicio2.batallaDeBotes(mapa,posicionesDeDisparosDePrueba)
        #Assert
        self.assertTrue(resultado == [])

    def testBatallaDeBotesRecibeUnMapaConEspaciosVaciosDeberiaRetornarUnaListaVacia(self):
        #Arrenge
        mapa = ["      "]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.batallaDeBotes(mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertEqual(resultado,[])

    def testBatallaDeBotesRecibeUnMapaNoValidDeberiaRetornarUnaListaVacia(self):
        #Arrange
        mapa = ["soy NO valido"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.batallaDeBotes(mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertTrue(resultado == [])

    def testBatallaDeBotesRecibeOtroMapaNoValidoDeberiaRetornarUnaListaVacia(self):
        #Arrenge
        mapa = ["yo","tambien","soy","invalido"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.batallaDeBotes(mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertEqual(resultado, [])

    def testBatallaDeBotesRecibeUnMapaConDistintasCantidadesDeElementosPorFilaDeberiaRetornarUnaListaVacia(self):
        #Arrenge
        mapa = ["b.b.","....","..bb","b.b"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.batallaDeBotes(mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertTrue(resultado == [])

    def testBatallaDeBotesRecibeUnMapaConPosicionesDeBarcosSinHundirDeberiaRetornarUnaListaConPosicionesDeBarcosHundidos(self):
        #Arrenge
        mapa = ["b.b..","b...b",".....","....b"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.batallaDeBotes(mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertEqual(resultado,[(2,1),(2,5)])

    def TestBatallaDeBotesRecibeUnMapaConPosicionesDeBarcosSinHundirUnaListaVaciaDeberiaRetornarUnaListaConPosicionesDeBarcosHundidos(self):
        #Arrenge
        mapa = ["b..","...","..b"]
        posicionesDeDisparosDePrueba = []
        # Act
        resultado = ejercicio2.batallaDeBotes(mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertTrue(resultado == [(1,1),(3,3)])
