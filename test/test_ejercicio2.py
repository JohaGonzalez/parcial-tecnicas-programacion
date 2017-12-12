import unittest
import ejercicio2

class ejercicio2_test (unittest.TestCase):

    def testBatallaDeBotesRecibeUnMapaVacioDeberiaRetornarListaVacia(self):
        #Arrange
        mapa=[]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        #Act
        resultado= ejercicio2.calcularPosicionesBotesNoHundidos(mapa, posicionesDeDisparosDePrueba)
        #Assert
        self.assertTrue(resultado == [])

    def testBatallaDeBotesRecibeOtroTipoDeMapaVacioDeberiaRetornarUnaListaVacia(self):
        #Arrange
        mapa = [""]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        #Act
        resultado= ejercicio2.calcularPosicionesBotesNoHundidos(mapa, posicionesDeDisparosDePrueba)
        #Assert
        self.assertTrue(resultado == [])

    def testBatallaDeBotesRecibeUnMapaConEspaciosVaciosDeberiaRetornarUnaListaVacia(self):
        #Arrenge
        mapa = ["      "]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.calcularPosicionesBotesNoHundidos(mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertEqual(resultado,[])

    def testBatallaDeBotesRecibeUnMapaNoValidoDeberiaRetornarUnaListaVacia(self):
        #Arrange
        mapa = ["soy NO valido"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.calcularPosicionesBotesNoHundidos(mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertTrue(resultado == [])

    def testBatallaDeBotesRecibeOtroMapaNoValidoDeberiaRetornarUnaListaVacia(self):
        #Arrenge
        mapa = ["yo","tambien","soy","invalido"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.calcularPosicionesBotesNoHundidos(mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertEqual(resultado, [])

    def testBatallaDeBotesRecibeUnMapaConDistintasCantidadesDeElementosPorFilaDeberiaRetornarUnaListaVacia(self):
        #Arrenge
        mapa = ["b.b.","....","..bb","b.b"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.calcularPosicionesBotesNoHundidos(mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertTrue(resultado == [])

    def testBatallaDeBotesRecibeUnMapaConPosicionesDeBarcosSinHundirDeberiaRetornarUnaListaConPosicionesDeBarcosNoHundidos(self):
        #Arrenge
        mapa = ["b.b..","b...b",".....","....b"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        # Act
        resultado = ejercicio2.calcularPosicionesBotesNoHundidos(mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertEqual(resultado,[(2,1),(2,5)])

    def TestBatallaDeBotesRecibeUnMapaConPosicionesDeBarcosSinHundirUnaListaVaciaDeberiaRetornarUnaListaConPosicionesDeBarcosNoHundidos(self):
        #Arrenge
        mapa = ["b..","...","..b"]
        posicionesDeDisparosDePrueba = []
        # Act
        resultado = ejercicio2.calcularPosicionesBotesNoHundidos(mapa, posicionesDeDisparosDePrueba)
        # Assert
        self.assertTrue(resultado == [(1,1),(3,3)])
