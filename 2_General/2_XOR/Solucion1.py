# XOR es un operador bit a bit que devuelve 0 si los bits son los mismos, y 1 de lo contrario. En los libros de texto, el operador XOR se denota por ⊕, pero en la mayoría de los desafíos y lenguajes de programación verá el cuidado ^ usado en su lugar.
# A	B	Salida
# 0	0	0
# 0	1	1
# 1	0	1
# 1	1	0
# Para números binarios más largos, XOR poco a poco: 0110 ^ 1010 = 1100. Podemos los enteros XOR convirtiendo primero el entero de decimal a binario. Podemos XOR cadenas convirtiendo primero cada carácter al número entero que representa el carácter Unicode.

# Dada la cuerda label, XOR cada carácter con el entero 13. Convierta estos enteros a una cadena y envíe el indicador como crypto{new_string}.

# NOTA: El Python pwntools la biblioteca tiene una conveniente xor() función que puede XOR juntos datos de diferentes tipos y longitudes. Pero primero, es posible que desee implementar su propia función para resolver esto.

# --------------------------SOLUCIÓN--------------------------
from pwn import *
def xor_cadena(s: str, key: int) -> str:
    return ''.join([chr(ord(c) ^ key) for c in s])

cadena_original = "label"
clave = 13

flag = xor_cadena(cadena_original, clave)
print("Flag:\n", flag.encode('utf-8'))