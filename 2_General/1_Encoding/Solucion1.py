# ASCII es un estándar de codificación de 7 bits que permite la representación de texto utilizando los enteros 0-127.

# Usando la siguiente matriz de enteros, convierta los números a sus caracteres ASCII correspondientes para obtener una bandera.

# [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# SOLUCION

vector=[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

resultado=[chr(num) for num in vector]
print("Caracteres en ASCII: ",resultado)

flag=''.join(resultado)
print("La bandera es:\n",flag)
