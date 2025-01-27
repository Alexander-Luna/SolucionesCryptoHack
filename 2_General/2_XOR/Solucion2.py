# En el último desafío, viste cómo XOR funcionaba a nivel de bits. En este, vamos a cubrir las propiedades de la operación XOR y luego las usaremos para deshacer una cadena de operaciones que han cifrado una bandera. Obtener una intuición de cómo funciona esto ayudará mucho cuando llegue a atacar criptosistemas reales más adelante, especialmente en la categoría de cifrados de bloque.

# Hay cuatro propiedades principales que debemos considerar cuando resolvemos desafíos utilizando el operador XOR

# Conmutativo: A ⊕ B = B ⊕ A
# Asociativo: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identidad: A ⊕ 0 = A
# Auto-Inverso: A ⊕ A = 0

# Vamos a romper esto. Conmutativo significa que el orden de las operaciones XOR no es importante. Asociativo significa que una cadena de operaciones se puede llevar a cabo sin orden (no tenemos que preocuparnos por los corchetes). La identidad es 0, por lo que XOR con 0 "no hace nada", y por último algo XOR'd con sí mismo devuelve cero.

# ¡Pongamos esto en práctica! A continuación se muestra una serie de salidas donde tres teclas aleatorias han sido XOR'd juntos y con la bandera. Utilice las propiedades anteriores para deshacer el cifrado en la línea final para obtener el indicador.

# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

# NOTA: Antes de XOR estos objetos, asegúrese de decodificar de hex a bytes.

# --------------------------SOLUCIÓN--------------------------
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2_xor_key1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2_xor_key3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag_xor_all = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

key2 = xor_bytes(key2_xor_key1, key1)

key3 = xor_bytes(key2_xor_key3, key2)

combined_key = xor_bytes(xor_bytes(key1, key2), key3)

flag = xor_bytes(flag_xor_all, combined_key)
print("Flag:\n", flag.decode())