def ligaDeFutbol(lista):
    tabla = []
    for tupla in lista:

        if tupla [1] == tupla [3]:
            equipo1empate = (tupla[0],1)
            equipo2empate = (tupla[2],1)
            tabla.append(equipo1empate)
            tabla.append(equipo2empate)

        if tupla[1] > tupla[3]:
            ganador = (tupla[0], 2)
            perdedor = (tupla[2], 0)
            tabla.append (ganador)
            tabla.append (perdedor)

        if tupla[1] < tupla[3]:
            ganador = (tupla[2], 2)
            perdedor = (tupla[0], 0)
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

def calculaSiHayEmpate(diccionario):
    puntajes = list(diccionario.values())
    puntajeGenerico = puntajes[0]
    for equipo in puntajes[1:]:
        if equipo != puntajeGenerico:
            return True
    return False


def eligeGanadorEnCasoDeEmpate(diccionario):
    diccionario = list(diccionario.keys())
    diccionario.sort()
    return diccionario[0]


def ganadorDeLiga(lista):
    if len(lista) < 1:
        return ""
    listaDeTuplas = ligaDeFutbol(lista)
    diccionario = DeTuplasADiccionario(listaDeTuplas)
    if calculaSiHayEmpate(diccionario) == False:
        return eligeGanadorEnCasoDeEmpate(diccionario)
    campeon = resultadosPartidosRealizados(diccionario)
    return campeon



def ejercicio3(var1):
    return ganadorDeLiga(var1)


assert (ejercicio3([]) == "")
assert (ejercicio3([("a", 1, "b", 0)]) == "a")
assert (ejercicio3([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
assert (ejercicio3([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")
assert (ejercicio3([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")