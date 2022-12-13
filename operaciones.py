class operaciones:
    def __init__(self, valor1, valor2):
        self.valora = valor1
        self.valorb = valor2

    def suma(self):
        x = self.valora
        y = self.valorb
        return x+y

    def resta(self):
        x = self.valora
        y = self.valorb
        return x-y

    def multiplicacion(self):
        x = self.valora
        y = self.valorb
        return x*y

    def division(self):
        x = self.valora
        y = self.valorb
        if y == 0:
            return 'no se puede dividir por cero'
        return x+y


def run():
    a = int(input('Ingresa un valor:  '))
    b = int(input('Ingresa otro valor: '))

    c = operaciones(a, b)

    print(f'El resultado de la suma es: {c.suma()}')
    print(f'El resultado de la resta es: {c.resta()}')
    print(f'El resultado de la multiplicaion es: {c.multiplicacion()}')
    print(f'El resultaado de la división es: {c.division()}')


if __name__ == '__main__':
    run()
