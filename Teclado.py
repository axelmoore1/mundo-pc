from DispositivosEntrada import DispositivosEntrada

class Teclado(DispositivosEntrada):

    contador_teclados = 0
    def __init__(self, marca, tipoEntrada):
        Teclado.contador_teclados += 1
        self._idTeclado = Teclado.contador_teclados
        super().__init__(marca, tipoEntrada)

    def __str__(self):
        return f'ID: {self._idTeclado}, Marca: {self._marca}, Entrada: {self._tipoEntrada}'

if __name__ == '__main__':
    teclado1 = Teclado('Noganet', 'usb')
    print(teclado1)
    teclado2 = Teclado('Hyperx', 'usb3')
    print(teclado2)
