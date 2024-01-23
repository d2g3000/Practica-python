import random
numero = random.randint(1, 10)
jugar = True
valores = []
turnos = 3
while (jugar):
    if len(valores) > 0:
        print(f'Los números usados son :{valores} quedan {turnos} turnos ')
    adivina = input('Ingresa un número para jugar: ')
    if adivina.isdigit() is False:
        print('solo admito números enteros')
        continue
    adivina = int(adivina)
    if adivina == numero:
        print('Felicitaciones ganaste!!!')
        volver = input('Si deseas jugar de nuevo presiona s : ')
        if volver == 's':
            jugar = True
            turnos = 3
            valores = []
            numero = random.randint(1, 10)
            continue
        break
    else:
        valores.append(adivina)
        print('Esta vez no acertaste!')
    turnos -= 1
    if turnos == 0:
        print('nos quedamos sin turnos')
        volver = input('Si deseas jugar de nuevo presiona s : ')
        if volver == 's':
            jugar = True
            turnos = 3
            valores = []
            numero = random.randint(1, 10)
            continue
        jugar = False
