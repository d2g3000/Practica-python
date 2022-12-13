# Declaramos la lista y se le asignan valores, aquí le asignaremos seis valores
lista = ["uno", "dos", "tres", "cuatro", "cinco", "seis"]

# Creamos una función que va a convertir de una lista a la otra de manera convencional
# a través de una condición en este caso que alguno de los elementos contenga la letra a.


def convertir_lista(x):
    lista_1 = []  # declaramos la nueva lista

    for i in x:  # recorremos la lista
        if "c" in i:  # Verificamos si la condición se cumple 
            lista_1.append(i)  # Agregamos el elemento i de la iteración.
            # Lo agregamos a la nueva lista que creamos que en este caso se llama lista_1
    return lista_1  # Devolvemos la lista

# Creamos otra función para utilizar listcomprehension y realizar el mismo procedimiento


def lista_listComprehension(x):

    # Declaramos y llenamos la lista si la condición se cumple
    lista_2 = [i for i in x if "c" in i]
    return lista_2  # Devolvemos la lista


def run():
    print(f' resultado metodo uno: {convertir_lista(lista)}')
    print(f' resultado metodo dos {lista_listComprehension(lista)}')


if __name__ == '__main__':
    run()
