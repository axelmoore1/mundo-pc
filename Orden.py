class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._idOrden = Orden.contador_ordenes
        self._computadoras = computadoras

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)


    def __str__(self):
        computadora_str = ''
        for computadora in self._computadoras:
            computadora_str += computadora.__str__()

        return f'''
            Orden: {self._idOrden}
            Computadoras: {computadora_str}
            '''

