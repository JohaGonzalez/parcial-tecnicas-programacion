def batallaDeBotes (columna,posicionADisparar ):
    mapa = []
    for i in range (len (columna)):
        if (columna [i] != ".") or (columna [i] != "b"):
            return []
    for fila in columna:
        if "b" in fila:
            posicion = 0
            for caracter in fila:

                if caracter == "b":
                    botes = (columna.index (fila)+ 1, posicion+1)
                    posicion = posicion + 1
                else:
                    posicion = posicion + 1
                    continue
                mapa.append (botes)
    for disparo in posicionADisparar:
        if disparo in mapa:
            mapa.remove (disparo)
    return mapa

def funcionResto1(tuplaAux):
    tuplaAux [0] = t [0] - 1
    tuplaAux[1] = t[1] - 1
    return tuplaAux

def funcionSuma1(tuplaAux1):
    tuplaAux1 [0] = t [0] + 1
    tuplaAux1 [1] = t[1] + 1
    return tuplaAux1

def tuplaAuxiliar ():
    for n in range (len(posicionesDeDisparosDePrueba)-1):
        tt= posicionesDeDisparosDePrueba [m]
        t = funcionResto1(tt)
        if m [tuplaAuxiliar(0)] [tuplaAuxiliar(1)] == "b"
            m [tuplaAuxiliar(0)] [tuplaAuxiliar(1)]== "."

def sobrevivientes ():
    listaSobrevivientes = []
    for i in range (len (m)):
        for j in range (len m [i])
            if (m [i] [j]== "b")
            t = (i,j)
        tAuxiliar = funcionSuma1(t)
    listaSobrevivientes.append (tAuxiliar)
    return sobrevivientes




#print(batallaDeBotes (["b.b..", "b...b",".....","....b"],[(1,1),(3,4),(1,3),(4,5)]))

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
#assert (ejercicio2(["b..","...","..b"],[]) == [(1,1),(3,3)])



#print (batallaDeBotes(["b.b..","b...b",".....","....b"], posicionesDeDisparosDePrueba))