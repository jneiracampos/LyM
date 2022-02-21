# Este es el conjunto de elementos no terminales del lenguaje


estructuras_control = ['if', 'loop', 'repeat', 'not']
comandos = ['move', 'turn', 'face', 'put', 'pick',
            'move-dir', 'run-dirs', 'move-face', 'defvar', 'skip', 'defun']
condiciones = ['-p', 'not']
turn_to = ['left', 'right', 'around']
face_to = ['north', 'east', 'south', 'west']
dir = ['front', 'right', 'left', 'back']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
              'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
objects = ['Ballons', 'Chips']


# Este es el alfabeto que contiene los elementos terminales del lenguaje


alfabeto = [estructuras_control, comandos, condiciones,
            turn_to, face_to, dir, numeros, abecedario, objects]


# Estas son las reglas de producción del lenguaje


def defvar(cadena, indice):

    fbf = 0
    evaluar = ['defvar']
    restante = len(cadena) - (indice + 1)

    if restante >= 3:
        for i in range(1, 4):
            sub_indice = indice + i
            ins = cadena[sub_indice]
            evaluar.append(ins)

        nombre_variable = evaluar[1]
        sintaxis = ['defvar', nombre_variable, numeros, ')']

        if len(evaluar) == 4:
            if evaluar[3] == sintaxis[3]:
                for numero in numeros:
                    if numero in evaluar[2]:
                        fbf = 1
                        break

    return fbf


def equals(cadena, indice):

    fbf = 0
    evaluar = ['=']
    restante = len(cadena) - (indice + 1)

    if restante >= 3:
        for i in range(1, 4):
            sub_indice = indice + i
            ins = cadena[sub_indice]
            evaluar.append(ins)

        nombre_variable = evaluar[1]
        sintaxis = ['=', nombre_variable, numeros, ')']

        if len(evaluar) == 4:
            if evaluar[3] == sintaxis[3]:
                for numero in numeros:
                    if numero in evaluar[2]:
                        fbf = 1
                        break

    return fbf


def move(cadena, indice):

    fbf = 0
    evaluar = ['move']
    sintaxis = ['move', numeros, ')']
    restante = len(cadena) - (indice + 1)

    if restante >= 2:
        for i in range(1, 3):
            sub_indice = indice + i
            ins = cadena[sub_indice]
            evaluar.append(ins)

        if len(evaluar) == 3:
            if evaluar[2] == sintaxis[2]:
                for numero in numeros:
                    if numero in evaluar[1]:
                        fbf = 1
                        break

    return fbf


def turn(cadena, indice):

    fbf = 0
    evaluar = ['turn']
    sintaxis = ['turn', ':', turn_to, ')']
    restante = len(cadena) - (indice + 1)

    if restante >= 3:
        for i in range(1, 4):
            sub_indice = indice + i
            ins = cadena[sub_indice]
            evaluar.append(ins)

        if len(evaluar) == 4:
            if evaluar[1] == sintaxis[1]:
                if evaluar[3] == sintaxis[3]:
                    for turn in turn_to:
                        if turn in evaluar[2]:
                            fbf = 1
                            break

    return fbf


def face(cadena, indice):

    fbf = 0
    evaluar = ['face']
    sintaxis = ['face', ':', face_to, ')']
    restante = len(cadena) - (indice + 1)

    if restante >= 3:
        for i in range(1, 4):
            sub_indice = indice + i
            ins = cadena[sub_indice]
            evaluar.append(ins)

        if len(evaluar) == 4:
            if evaluar[1] == sintaxis[1]:
                if evaluar[3] == sintaxis[3]:
                    for turn in face_to:
                        if turn in evaluar[2]:
                            fbf = 1

    return fbf


def put(cadena, indice):

    fbf = 0
    evaluar = ['put']
    sintaxis = ['put', objects, numeros, ')']
    restante = len(cadena) - (indice + 1)

    if restante >= 3:
        for i in range(1, 4):
            sub_indice = indice + i
            ins = cadena[sub_indice]
            evaluar.append(ins)

        if len(evaluar) == 4:
            if evaluar[3] == sintaxis[3]:
                for element in objects:
                    if evaluar[1] == element:
                        for numero in numeros:
                            if numero in evaluar[2]:
                                fbf = 1
                                break
                    break

    return fbf


def pick(cadena, indice):

    fbf = 0
    evaluar = ['pick']
    sintaxis = ['pick', objects, numeros, ')']
    restante = len(cadena) - (indice + 1)

    if restante >= 3:
        for i in range(1, 4):
            sub_indice = indice + i
            ins = cadena[sub_indice]
            evaluar.append(ins)

        if len(evaluar) == 4:
            if evaluar[3] == sintaxis[3]:
                for element in objects:
                    if evaluar[1] == element:
                        for numero in numeros:
                            if numero in evaluar[2]:
                                fbf = 1
                                break
                    break

    return fbf


def move_dir(cadena, indice):

    fbf = 0
    evaluar = ['move-dir']
    sintaxis = ['move-dir', numeros, ':', dir, ')']
    restante = len(cadena) - (indice + 1)

    if restante >= 4:
        for i in range(1, 5):
            sub_indice = indice + i
            ins = cadena[sub_indice]
            evaluar.append(ins)

        if len(evaluar) == 5:
            if evaluar[2] == sintaxis[2]:
                if evaluar[4] == sintaxis[4]:
                    for numero in numeros:
                        if numero in evaluar[1]:
                            for element in dir:
                                if evaluar[3] == element:
                                    fbf = 1
                                    break
                        break

    return fbf


def run_dirs(cadena, indice):

    fbf = 0
    evaluar = ['run-dirs']
    sintaxis = ['run-dirs', ':', dir, ')']
    restante = len(cadena) - (indice + 1)

    if restante >= 3:
        for i in range(1, 4):
            sub_indice = indice + i
            ins = cadena[sub_indice]
            evaluar.append(ins)

        if len(evaluar) == 4:
            if evaluar[1] == sintaxis[1]:
                if evaluar[3] == sintaxis[3]:
                    for element in dir:
                        if evaluar[2] == element:
                            fbf = 1
                            break

    return fbf


def move_face(cadena, indice):

    fbf = 0
    evaluar = ['move-face']
    sintaxis = ['move-face', numeros, ':', face_to, ')']
    restante = len(cadena) - (indice + 1)

    if restante >= 4:
        for i in range(1, 5):
            sub_indice = indice + i
            ins = cadena[sub_indice]
            evaluar.append(ins)

        if len(evaluar) == 5:
            if evaluar[2] == sintaxis[2]:
                if evaluar[4] == sintaxis[4]:
                    for numero in numeros:
                        if numero in evaluar[1]:
                            for element in face_to:
                                if evaluar[3] == element:
                                    fbf = 1
                                    break
                        break

    return fbf


def skip(cadena, indice):

    fbf = 0
    evaluar = ['skip']
    sintaxis = ['skip', ')']
    restante = len(cadena) - (indice + 1)

    if restante >= 1:
        for i in range(1, 2):
            sub_indice = indice + i
            ins = cadena[sub_indice]
            evaluar.append(ins)

        if len(evaluar) == 2:
            if evaluar[1] == sintaxis[1]:
                fbf = 1

    return fbf


# Estas son las estructuras de control


def if_condicional(cadena, indice):

    fbf = 0
    evaluar = ['if']
    lista = []
    contar = 0
    i = 0
    parentesisI = 1
    parentesisD = 0
    sub_indice = indice

    while (parentesisI != parentesisD):
        sub_indice += 1
        if sub_indice < len(cadena):
            ins = cadena[sub_indice]
            evaluar.append(ins)
            if ins == '(':
                parentesisI += 1
            elif ins == ')':
                parentesisD += 1
        else:
            parentesisD += 1

    while i < len(evaluar):
        if evaluar[i] == 'defvar':
            retorno = defvar(evaluar, i)
            lista.append(retorno)
        elif evaluar[i] == '=':
            retorno = equals(evaluar, i)
            lista.append(retorno)
        elif evaluar[i] == 'move':
            retorno = move(evaluar, i)
            lista.append(retorno)
        elif evaluar[i] == 'turn':
            retorno = turn(evaluar, i)
            lista.append(retorno)
        elif evaluar[i] == 'face':
            retorno = face(evaluar, i)
            lista.append(retorno)
        elif evaluar[i] == 'put':
            retorno = put(evaluar, i)
            lista.append(retorno)
        elif evaluar[i] == 'pick':
            retorno = pick(evaluar, i)
            lista.append(retorno)
        elif evaluar[i] == 'move-dir':
            retorno = move_dir(evaluar, i)
            lista.append(retorno)
        elif evaluar[i] == 'run-dirs':
            retorno = run_dirs(evaluar, i)
            lista.append(retorno)
        elif evaluar[i] == 'move-face':
            retorno = move_face(evaluar, i)
            lista.append(retorno)
        elif evaluar[i] == 'skip':
            retorno = skip(evaluar, i)
            lista.append(retorno)
        elif evaluar[i] == 'not':
            retorno = _p(cadena, i)
            lista.append(retorno)
        elif '-p' in evaluar[i]:
            retorno = _p(cadena, i)
            lista.append(retorno)

        i += 1

    for element in lista:
        contar += element

    if contar == len(lista):
        fbf = 1

    return fbf


def loop(cadena, indice):

                        

    return fbf


def repeat(cadena, indice):
    fbf = 0
    evaluar = ['repeat']
    sintaxis = ['repeat', numeros, comandos, ")"]
    restante = len(cadena) - (indice + 1)

    if restante >= 3:
        for i in range(1, 4):
            sub_indice = indice + i
            ins = cadena[sub_indice]
            evaluar.append(ins)

        nombre_variable = evaluar[1]
        sintaxis = ['repeat', numeros, comandos, ")"]

        if len(evaluar) == 4:
            if evaluar[2] in numeros:
                if evaluar[3] in comandos:
                    fbf = 1
                             
    pass


def defun(cadena, indice):
    fbf = 0
    evaluar = ['defun']
    restante = len(cadena) - (indice + 1)

    if restante >= 2:
        for i in range(1, 3):
            sub_indice = indice + i
            ins = cadena[sub_indice]
            evaluar.append(ins)

        nombre_variable = evaluar[1]
        sintaxis = ['defun', (_p(cadena, indice)), ")"]

        if len(evaluar) == 3:
            if (_p(cadena, indice)) == 1: 
                fbf = 1
        

    return fbf


def _p(cadena, indice):

    fbf = 0
    evaluar = []
    parentesisI = 1
    parentesisD = 0
    sub_indice = indice

    while (parentesisI != parentesisD):
        sub_indice += 1
        if sub_indice < len(cadena):
            ins = cadena[sub_indice]
            evaluar.append(ins)
            if ins == '(':
                parentesisI += 1
            elif ins == ')':
                parentesisD += 1
        else:
            parentesisD += 1

    for element in evaluar:
        for condicion in condiciones:
            if condicion in element:
                fbf = 1
            else:
                fbf = 0

    return fbf


# Implementación de los métodos anteriores


def lectura(archivo):

    file = open(str(archivo) + 'r')
    cadena = []
    lineas = file.read().splitlines()
    for linea in lineas:
        auxiliar = linea.split()
        for palabra in auxiliar:
            caracteres = list(palabra)
            for caracter in caracteres:
                if '(' == caracter:
                    cadena.append(caracter)
                if ':' == caracter:
                    cadena.append(caracter)
            if '(' in palabra:
                nueva = palabra.strip('(')
                if ':' in palabra:
                    nueva1 = nueva.strip(':')
                    if ')' in palabra:
                        nueva2 = nueva1.strip(')')
                        if nueva2 != '':
                            cadena.append(nueva2)
                    else:
                        if nueva1 != '':
                            cadena.append(nueva1)
                elif ')' in palabra:
                    nueva1 = nueva.strip(')')
                    if nueva1 != '':
                        cadena.append(nueva1)
                else:
                    if nueva != '':
                        cadena.append(nueva)
            elif ':' in palabra:
                nueva = palabra.strip(':')
                if ')' in palabra:
                    nueva1 = nueva.strip(')')
                    if nueva1 != '':
                        cadena.append(nueva1)
                else:
                    if nueva != '':
                        cadena.append(nueva)
            elif ')' in palabra:
                nueva = palabra.strip(')')
                if nueva != '':
                    cadena.append(nueva)
            else:
                if palabra != '':
                    cadena.append(palabra)
            for caracter in caracteres:
                if ')' in caracter:
                    cadena.append(')')

    file.close()

    return cadena


def implementar(archivo):

    cadena = lectura(archivo)
    sintaxis = []
    contar = 0
    parentesis = 0
    parentesisI = 0
    parentesisD = 0
    indice = 0

    while indice < len(cadena):
        if cadena[indice] == '(':
            parentesisI += 1
        elif cadena[indice] == ')':
            parentesisD += 1
        elif cadena[indice] == 'defvar':
            retorno = defvar(cadena, indice)
            sintaxis.append(retorno)
        elif cadena[indice] == '=':
            retorno = equals(cadena, indice)
            sintaxis.append(retorno)
        elif cadena[indice] == 'move':
            retorno = move(cadena, indice)
            sintaxis.append(retorno)
        elif cadena[indice] == 'turn':
            retorno = turn(cadena, indice)
            sintaxis.append(retorno)
        elif cadena[indice] == 'face':
            retorno = face(cadena, indice)
            sintaxis.append(retorno)
        elif cadena[indice] == 'put':
            retorno = put(cadena, indice)
            sintaxis.append(retorno)
        elif cadena[indice] == 'pick':
            retorno = pick(cadena, indice)
            sintaxis.append(retorno)
        elif cadena[indice] == 'move-dir':
            retorno = move_dir(cadena, indice)
            sintaxis.append(retorno)
        elif cadena[indice] == 'run-dirs':
            retorno = run_dirs(cadena, indice)
            sintaxis.append(retorno)
        elif cadena[indice] == 'move-face':
            retorno = move_face(cadena, indice)
            sintaxis.append(retorno)
        elif cadena[indice] == 'skip':
            retorno = skip(cadena, indice)
            sintaxis.append(retorno)

        indice += 1

    if parentesisI == parentesisD:
        parentesis = 1

    for element in sintaxis:
        contar += element

    if contar == len(sintaxis):
        sintaxis = 1
    else:
        sintaxis = 0

    sintaxis *= parentesis

    if sintaxis == 0:
        mensaje = 'Hay un problema de sintaxis en el código'
    else:
        mensaje = 'El código se compiló correctamente'

    return mensaje
