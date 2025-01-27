# Otro esquema de codificación común es Base64, que nos permite representar datos binarios como una cadena ASCII utilizando un alfabeto de 64 caracteres. Un carácter de una cadena Base64 codifica 6 dígitos binarios (bits), por lo que 4 caracteres de Base64 codifican tres bytes de 8 bits.

# Base64 se usa más comúnmente en línea, por lo que los datos binarios, como las imágenes, se pueden incluir fácilmente en archivos HTML o CSS.

# Tome la cuerda hexagonal a continuación, decodificar en bytes y luego codificar en Base64.

# 72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf

#  NOTA: En Python, tras importar el módulo base64 con import base64, puedes usar el base64.b64encode() función. Recuerde decodificar el hexágono primero como dice la descripción del desafío.

import base64
cadenaHexa="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
decode=bytes.fromhex(cadenaHexa)
flag=base64.b64encode(decode).decode('utf-8')
print("La bandera es:\n",flag)