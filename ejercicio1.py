def rotacionesDePalabra(palabra):
    rotacion = []
    lista = "no_espacio"
    for letra in palabra:
        if letra == " ":
            rotacion.append (letra)
        else:
            rotacion.append(lista)
    if len (palabra) < 1 or lista not in rotacion:
        return []
    rotacion2 = []
    rotar = len (palabra)
    ultimaLetra = -1
    for i in range (rotar):
        rotar1 = palabra [ultimaLetra:] + palabra [:ultimaLetra]
        rotacion2.append (rotar1)
        ultimaLetra= ultimaLetra - 1
    rotacion2 = rotacion2 [::-1]
    return rotacion2

#print(rotacionesDePalabra("rotar"))

def ejercicio1(palabra):
    return rotacionesDePalabra(palabra)

assert (ejercicio1("") == [])
assert (ejercicio1("     ") == [])
assert (ejercicio1("a") == ['a'])
assert (ejercicio1("ab") == ['ab','ba'])
assert (ejercicio1("paz") == ['paz','azp','zpa'])
assert (ejercicio1("so l") == ['so l','o ls',' lso','lso '])
assert (ejercicio1("rotar") == ['rotar','otarr','tarro','arrot','rrota'])
