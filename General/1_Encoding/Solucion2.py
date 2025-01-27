# Cuando ciframos algo, el texto cifrado resultante comúnmente tiene bytes que no son caracteres ASCII imprimibles. Si queremos compartir nuestros datos cifrados, es común codificarlos en algo más fácil de usar y portátil en diferentes sistemas.

# Hexadecimal se puede usar de tal manera para representar cadenas ASCII. Primero, cada letra se convierte en un número ordinal de acuerdo con la tabla ASCII (como en el desafío anterior). Luego, los números decimales se convierten en números base-16, también conocidos como hexadecimales. Los números se pueden combinar juntos, en una cadena hexagonal larga.

# A continuación se incluye una bandera codificada como una cadena hexagonal. Decodifique esto de nuevo en bytes para obtener la bandera.

# 63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d

# NOTA: En Python, el bytes.fromhex() la función se puede utilizar para convertir hex a bytes. El .hex() el método de instancia puede ser llamado en cadenas de bytes para obtener la representación hexadecimal.

cadenaHexa="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
flag=bytes.fromhex(cadenaHexa).decode('utf-8')
print("La bandera es:\n",flag)