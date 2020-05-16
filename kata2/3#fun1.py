'''
Escribir una función que calcule el área de un circulo y otra que calcule el volumen de un cilindro
usando la primera función.
'''

def circle_area(radius):
    '''
    Función que calcula el área de un círculo.
    Parámetros
    radius: Es el radio del circulo.
    Devuelve el área del circulo de radio radius.
    '''
    pi = 3.1415
    return 2*pi*radius**2

def cilinder_volumen(radius, high):
    '''
    Fumción que calcula el volumen de un cilindro.
    Parámetros
    radius: Es el radio de la base del cilindro.
    Devuelve el volumen del cilindro de radio radius y altura high.
    '''

    return circle_area(radius)*high

print(cilinder_volumen(3, 5))