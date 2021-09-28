from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora():
    contador_computadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._idComputadoras = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        Nombre PC: {self._nombre} ID: {self._idComputadoras}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton:   {self._raton}
        '''
if __name__ == '__main__':
    teclado1 = Teclado('Hp', 'Usb')
    monitor1 = Monitor('Asus', 22)
    raton1 = Raton('HyperX', 'usb')
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)
