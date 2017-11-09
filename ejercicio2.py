def batallaDeBotes (columna,posicionADisparar ):
    mapa = []
    for i in range (len (columna)):
        if (columna [i] != ".") or (columna [i] != "b"):
            return []
    for fila in columna:
        if "b" in fila:
            posicion = 0
            for x in fila:
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
#assert (ejercicio2(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
#(ejercicio2(["b..","...","..b"],[]) == [(1,1),(3,3)])

