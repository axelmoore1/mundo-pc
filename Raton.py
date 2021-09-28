from DispositivosEntrada import DispositivosEntrada

class Raton(DispositivosEntrada):


    contador_ratones = 0
    def __init__(self, marca, tipoEntrada):
        Raton.contador_ratones += 1  #contador de ratones
        self._idRaton = Raton.contador_ratones
        super().__init__(marca, tipoEntrada) #aca pasa los valores

    def __str__(self):
        return f'ID {self._idRaton}, Marca: {self._marca}, Entrada: {self._tipoEntrada}'
if __name__ == '__main__':
    raton1 = Raton('HP', 'usb')
    print(raton1)
    raton2 = Raton('Acer', 'usb')
    print(raton2)


