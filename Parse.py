# Este es el conjunto de elementos no terminales del lenguaje


estructuras_control = ['if', 'loop', 'repeat', 'not']
comandos = ['move', 'turn', 'face', 'put', 'pick',
            'move-dir', 'run-dirs', 'move-face', 'defvar', 'skip', 'defun']
condiciones = ['facing-p', 'can-put-p', 'can-pick-p', 'can-move-p', '-p']
operaciones = ['=', '(', ')', ':']
turn_to = ['left', 'right', 'around']
face_to = ['north', 'east', 'south', 'west']
dir = ['front', 'right', 'left', 'back']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
              'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Este es el alfabeto que contiene los elementos terminales del lenguaje


alfabeto = [estructuras_control, comandos, condiciones,
            operaciones, turn_to, face_to, dir, numeros, abecedario]


# Estas son las reglas de producción del lenguaje


def parentesis(cadena):
    pass


def defvar(cadena):
    pass


def equals(cadena):
    pass


def move(cadena):
    pass


def turn(cadena):
    pass


def face(cadena):
    pass


def put(cadena):
    pass


def pick(cadena):
    pass


def move_dir(cadena):
    pass


def run_dirs(cadena):
    pass


def move_face(cadena):
    pass


def skip(cadena):
    pass


def if_condicional(cadena):
    pass


def loop(cadena):
    pass


def repeat(cadena):
    pass


def defun(cadena):
    pass


def _p(cadena):
    pass


# Implementación


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


def implementar(cadena):

    if alfabeto[1][8] in cadena:
        defvar(cadena)
    if alfabeto[3][0]:
        equals(cadena)
