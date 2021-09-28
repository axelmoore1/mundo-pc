class Monitor:
    contador_monitores = 0
    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self._idMonitor = Monitor.contador_monitores
        self._marca = marca
        self._tamanio = tamanio

    def __str__(self):
        return f'ID: {self._idMonitor}, Marca: {self._marca}, Tamaño: {self._tamanio}'

if __name__ == '__main__':
    monitor1 = Monitor('Noganet', 15)
    print(monitor1)
    monitor2 = Monitor('Hyperx', 15)
    print(monitor2)

