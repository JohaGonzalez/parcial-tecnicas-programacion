
def mapaInvalido(mapa):

    if mapa == []:
        return True

    longitudFilas = []

    for index, fila in enumerate(mapa):

        longitudFilas.append(len(fila))

        if longitudFilas[index] == 0:
            return True

        if index > 0:
            if longitudFilas[index] != longitudFilas[index-1]:
                return True

        for letra in fila:
            if letra != '.' and letra != 'b':
                return True

    return False


def convertirMapaAMapaBooleano(mapa):

    mapaBooleano =[]

    for fila in mapa:

        filaBooleana = []

        for letra in fila:
            if letra == '.':
                filaBooleana.append(False)
            else:
                filaBooleana.append(True)

        mapaBooleano.append(filaBooleana)

    return mapaBooleano

"""
PRE:
POST: Modifica el mapa pasado por parametro
"""
def disparAlMapa(mapa,posicionesADisparar):

    for disparo in posicionesADisparar:
        fila = disparo[0]-1
        columna = disparo[1]-1
        mapa[fila][columna] = False

def obtenerPosicionesBarcosNoHundidos(mapa):

    posiciones = []

    for indexFila, fila in enumerate(mapa):
        for indexColumna, columna in enumerate(fila):
            if columna:
                posicion = (indexFila+1,indexColumna+1)
                posiciones.append(posicion)


    return posiciones

def batallaDeBotes (mapa,posicionADisparar):

    if mapaInvalido(mapa):
        return[]

    mapaConBooleanos = convertirMapaAMapaBooleano(mapa)
    disparAlMapa(mapaConBooleanos,posicionADisparar)
    posicionesBarcosSinHundir = obtenerPosicionesBarcosNoHundidos(mapaConBooleanos)

    return posicionesBarcosSinHundir


def ejercicio2(var1,var2):
    return batallaDeBotes(var1,var2)

posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

assert (ejercicio2([],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2([""],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["      "],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["soy NO valido"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["yo","tambien","soy","invalido"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
assert (ejercicio2(["b..","...","..b"],[]) == [(1,1),(3,3)])
