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
object = ['Ballons', 'Chips']


# Este es el alfabeto que contiene los elementos terminales del lenguaje


alfabeto = [estructuras_control, comandos, condiciones,
            operaciones, turn_to, face_to, dir, numeros, abecedario, object]


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


def equals(cadena):

    sintaxis = ['=', alfabeto, numeros]

    return sintaxis


def move(cadena):

    sintaxis = ['move', numeros]

    return sintaxis


def turn(cadena):

    sintaxis = ['turn', ':', turn_to]

    return sintaxis


def face(cadena):

    sintaxis = ['face', ':', face_to]

    return sintaxis


def put(cadena):

    sintaxis = ['put', object, numeros]

    return sintaxis


def pick(cadena):

    sintaxis = ['pick', object, numeros]

    return sintaxis


def move_dir(cadena):

    sintaxis = ['move-dir', numeros, ':', dir]

    return sintaxis


def run_dirs(cadena):

    sintaxis = ['run-dirs', ':', dir]

    return sintaxis


def move_face(cadena):

    sintaxis = ['move-face', numeros, ':', face_to]

    return sintaxis


def skip(cadena):

    sintaxis = ['skip']

    return sintaxis


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
