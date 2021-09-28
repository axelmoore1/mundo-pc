from Computadora import Computadora
from Monitor import Monitor
from Orden import Orden
from Raton import Raton
from Teclado import Teclado


teclado1 = Teclado('Hp', 'Usb')
monitor1 = Monitor('Asus', 22)
raton1 = Raton('HyperX', 'usb')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

print(computadora1)

compus = [computadora1]
orden1 = Orden(compus)