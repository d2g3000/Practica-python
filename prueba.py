class ejemplo:
    def publico(self):
        print("publico")

    def __privado(self):
        print("privado")


prueba = ejemplo()
prueba.publico()
prueba._ejemplo__privado()
