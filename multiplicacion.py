def multiplicacion(a, b):
    return a*b


def pedir_valores():
    valor1 = int(input('Ingresa el primer valor :'))
    valor2 = int(input('Ingresa el segundo valor: '))
    resultado = multiplicacion(valor1, valor2)
    print(
        f'El resultado des multiplicar {valor1} por {valor2} es: {resultado}')


def run():
    pedir_valores()


if __name__ == '__main__':
    run()
