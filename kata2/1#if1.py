"""
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprime por pantalla si la
contraseña introducida por le usuario conincide con la guardada en la variable
sin tener en cuenta mayúsculas y minúsculas.
"""

password = "contraseña"

password_del_usuario = input("Introduzca la contraseña: ")
#convertimos el texto a minúsculas
password_del_usuario = password_del_usuario.lower()

if password == password_del_usuario:
    print("El password es correcto")
else:
    print("El password no coincide")