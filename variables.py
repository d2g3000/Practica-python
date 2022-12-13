
# tipos de variables

cadena = 'Hola mundo'  # cadena de caracteres
entero = 1  # int
flotante = 10.5  # float
booleano = False  # booleano
lista = [1, 2, 3, 4, 5, 1, 2, 8, 'f']  # lista
diccionario = {'a': 1, 'b': 2, 'c': 5}
tupla = (2, 2, 3, 5, 4, 'f')
sett = {2, 5, 4, 5, 4, 'f'}

# obtener nombre de la variable


def nombre_variable(variable):
    dg = globals()

    return [var for var in dg if dg[var] is variable]


def imprimir():

    listado = [cadena, entero, flotante,
               booleano, lista, diccionario, tupla, sett]
    for i in listado:
        print(
            f' la variable {nombre_variable(i)} es de tipo {type(i)} y su contenido es: {i}')


def run():
    imprimir()


if __name__ == '__main__':
    run()
