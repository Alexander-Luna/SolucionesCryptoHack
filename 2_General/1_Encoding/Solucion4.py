# Los criptosistemas como RSA funcionan en números, pero los mensajes están formados por caracteres. ¿Cómo debemos convertir nuestros mensajes en números para que se puedan aplicar operaciones matemáticas?

# La forma más común es tomar los bytes ordinales del mensaje, convertirlos en hexadecimal y concatenar. Esto puede interpretarse como un número base-16/hexadecimal, y también representado en base-10/decimal.

# Para ilustrar:

# mensaje: HOLA
# bytes Ascii: [72, 69, 76, 76, 79]
# bytes hexagonales: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
# base-16:0x48454c4c4f
# base-10: 310400273487

#  NOTA: La biblioteca PyCryptodome de Python implementa esto con los métodos bytes_to_long() y long_to_bytes(). Primero tendrá que instalar PyCryptodome e importarlo con from Crypto.Util.number import *. Para más detalles, consulte el PREGUNTAS FRECUENTES.

from Crypto.Util.number import *
enc=11515195063862318899931685488813747395775516287289682636499965282714637259206269
bytes=long_to_bytes(enc)
flag=bytes.decode('utf-8')
print(flag)