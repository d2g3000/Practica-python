def holamundo(user):
    a = user
    print(f'hola {a} como estas, este es tu primer hola mundo ')


def solicitar_nombre():
    nombre = input('Ingresa tu nombre: ')
    holamundo(nombre)


def run():
    solicitar_nombre()


if __name__ == '__main__':
    run()
