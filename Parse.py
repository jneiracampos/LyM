# Este es el conjunto de elementos no terminales del lenguaje


estructuras_control = ['if', 'loop', 'repeat', 'not']
comandos = ['move', 'turn', 'face', 'put', 'pick',
            'move-dir', 'run-dirs', 'move-face', 'defvar', 'skip', 'defun']
condiciones = ['-p', 'not']
operaciones = ['=', '(', ')', ':']
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
            operaciones, turn_to, face_to, dir, numeros, abecedario, objects]


# Estas son las reglas de producción del lenguaje


def defvar(cadena, indice):

    fbf = 0
    evaluar = ['defvar']

    for i in range(1, 4):
        sub_indice = indice + i
        ins = cadena[sub_indice]
        evaluar.append(ins)

    nombre_variable = evaluar[1]

    sintaxis = ['defvar', nombre_variable, numeros, ')']

    if evaluar[3] == sintaxis[3]:
        for numero in numeros:
            if numero in evaluar[2]:
                fbf = 1

    return fbf, nombre_variable


def equals(cadena, indice):

    fbf = 0
    evaluar = ['=']

    for i in range(1, 4):
        sub_indice = indice + i
        ins = cadena[sub_indice]
        evaluar.append(ins)

    nombre_variable = evaluar[1]

    sintaxis = ['=', nombre_variable, numeros, ')']

    if evaluar[3] == sintaxis[3]:
        for numero in numeros:
            if numero in evaluar[2]:
                fbf = 1

    return fbf, nombre_variable


def move(cadena, indice):

    fbf = 0
    evaluar = ['move']

    for i in range(1, 3):
        sub_indice = indice + i
        ins = cadena[sub_indice]
        evaluar.append(ins)

    sintaxis = ['move', numeros, ')']

    if evaluar[2] == sintaxis[2]:
        for numero in numeros:
            if numero in evaluar[1]:
                fbf = 1

    return fbf


def turn(cadena, indice):

    fbf = 0
    evaluar = ['turn']

    for i in range(1, 4):
        sub_indice = indice + i
        ins = cadena[sub_indice]
        evaluar.append(ins)

    sintaxis = ['turn', ':', turn_to, ')']

    if evaluar[1] == sintaxis[1]:
        if evaluar[3] == sintaxis[3]:
            for turn in turn_to:
                if turn in evaluar[2]:
                    fbf = 1

    return fbf


def face(cadena, indice):

    fbf = 0
    evaluar = ['face']

    for i in range(1, 4):
        sub_indice = indice + i
        ins = cadena[sub_indice]
        evaluar.append(ins)

    sintaxis = ['face', ':', face_to, ')']

    if evaluar[1] == sintaxis[1]:
        if evaluar[3] == sintaxis[3]:
            for turn in face_to:
                if turn in evaluar[2]:
                    fbf = 1

    return fbf


def put(cadena, indice):

    fbf = 0
    evaluar = ['put']

    for i in range(1, 4):
        sub_indice = indice + i
        ins = cadena[sub_indice]
        evaluar.append(ins)

    sintaxis = ['put', objects, numeros, ')']

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

    for i in range(1, 4):
        sub_indice = indice + i
        ins = cadena[sub_indice]
        evaluar.append(ins)

    sintaxis = ['pick', objects, numeros, ')']

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

    for i in range(1, 5):
        sub_indice = indice + i
        ins = cadena[sub_indice]
        evaluar.append(ins)

    sintaxis = ['move-dir', numeros, ':', dir, ')']

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

    for i in range(1, 4):
        sub_indice = indice + i
        ins = cadena[sub_indice]
        evaluar.append(ins)

    sintaxis = ['run-dirs', ':', dir, ')']

    if evaluar[1] == sintaxis[1]:
        if evaluar[3] == sintaxis[3]:
            for element in dir:
                if evaluar[2] == element:
                    fbf = 1
                    break

    return fbf


def move_face(cadena, indice):

    fbf = 0
    evaluar = ['move-dir']

    for i in range(1, 5):
        sub_indice = indice + i
        ins = cadena[sub_indice]
        evaluar.append(ins)

    sintaxis = ['move-face', numeros, ':', face_to, ')']

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

    for i in range(1, 2):
        sub_indice = indice + i
        ins = cadena[sub_indice]
        evaluar.append(ins)

    sintaxis = ['skip', ')']

    if evaluar[1] == sintaxis[1]:
        fbf = 1

    return fbf


# Estas son las estructuras de control


def if_condicional(elemento, comando, comando1):

    sintaxis = ['if', '(', condiciones, ')', '(',
                comando, ')', '(', comando1, ')']

    return sintaxis


def loop(cadena):
    pass


def repeat(cadena):
    pass


def defun(cadena):
    pass


def _p(cadena):
    pass


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
    sintaxis = 0
    parentesisI = 0
    parentesisD = 0
    indice = 0

    while indice < len(cadena):
        if cadena[indice] == '(':
            parentesisI += 1
        elif cadena[indice] == ')':
            parentesisD += 1
        elif cadena[indice] == 'defvar':
            defvar(cadena, indice)

    if parentesisI == parentesisD:
        sintaxis = 1

    return sintaxis
