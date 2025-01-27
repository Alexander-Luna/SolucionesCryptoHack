# He encriptado la bandera con mi clave secreta, nunca podrás adivinarla.

# ¡Recuerde el formato de la bandera y cómo podría ayudarlo en este desafío!


# 0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104

# --------------------------SOLUCIÓN--------------------------

hex_string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
ciphertext = bytes.fromhex(hex_string)

known_prefix = b"crypto{"

partial_key = bytes([ciphertext[i] ^ known_prefix[i] for i in range(len(known_prefix))])

full_key = (partial_key + b'y').decode()  # Resultado: 'myXORkey'

flag = bytes([ciphertext[i] ^ ord(full_key[i % len(full_key)]) for i in range(len(ciphertext))])
print("Flag:\n", flag.decode())