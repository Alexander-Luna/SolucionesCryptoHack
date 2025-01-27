# Para los próximos desafíos, usarás lo que acabas de aprender para resolver algunos rompecabezas XOR más.

# He ocultado algunos datos usando XOR con un solo byte, pero ese byte es un secreto. No olvides decodificar desde hex primero.

# 73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d

# --------------------------SOLUCIÓN--------------------------

hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
ciphertext = bytes.fromhex(hex_string)

for key in range(256):
    decrypted = bytes([b ^ key for b in ciphertext])
    if decrypted.startswith(b'crypto{'):
        print(f"Clave: 0x{key:02x} → {key}")
        print(f"Flag: {decrypted.decode()}")
        break