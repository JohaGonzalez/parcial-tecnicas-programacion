def ligaDeFutbol(lista):
    tabla = []
    if lista [0] [1] == lista [0] [3]:
        return [(lista [0] [0], 1), (lista [0] [2], 1)]
    if lista [0] [1] >lista [0] [3]:
        ganador = (lista [0] [0], 2)
        perdedor = (lista [0] [2], 0)
        tabla.append (ganador)
        tabla.append (perdedor)
    if lista [0] [1] < lista [0] [3]:
        ganador = (lista [0] [2], 2)
        perdedor = (lista [0] [0], 0)
        tabla.append (ganador)
        tabla.append (perdedor)
    return tabla

def DeTuplasADiccionario(lista):
    diccionario = {}
    for tupla in lista:
        diccionario[tupla[0]] = tupla[1]
    return diccionario

def resultadosPartidosRealizados(diccionario):
    puntaje = diccionario.values()
    maximo = max(puntaje)
    for equipo in diccionario:
        if diccionario[equipo] == maximo:
            return equipo

def ganadorDeLiga(lista):
    if len(lista) < 1:
        return ""
    listaDeTuplas = ligaDeFutbol(lista)
    diccionario = DeTuplasADiccionario(listaDeTuplas)
    campeon = resultadosPartidosRealizados(diccionario)
    return campeon

assert (ganadorDeLiga([]) == "")
assert (ganadorDeLiga([("a", 1, "b", 0)]) == "a")
assert (ganadorDeLiga([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
#assert (ganadorDeLiga([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")
#assert (ganadorDeLiga([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")

#print (calculaEquipoGanador([("Barcelona",3,"Real Madrid",2)]))
#print (calculaEquipoGanador([("Barcelona",3,"Real Madrid",3)]))

"""def ejercicio3(var1):
    return calculaGanadorLigaFutbol(var1)


assert (ejercicio3([]) == "")
assert (ejercicio3([("a", 1, "b", 0)]) == "a")
assert (ejercicio3([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
assert (ejercicio3([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")
assert (ejercicio3([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")
"""