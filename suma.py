def suma(a, b):
    return a+b


def pedir_valores():
    valor1 = int(input('ingresa el primer valor :'))
    valor2 = int(input('ingresa el segundo valor: '))
    resultado = suma(valor1, valor2)
    print(f'El resultado es: {resultado}')


def run():
    pedir_valores()


if __name__ == '__main__':
    run()
