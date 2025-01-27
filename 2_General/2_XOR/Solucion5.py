# ¡He escondido dos imágenes geniales de XOR con la misma clave secreta para que no puedas verlas!

# Este desafío requiere realizar un XOR visual entre los bytes RGB de las dos imágenes, no un XOR de todos los bytes de datos de los archivos.


# Archivos de desafío:
#   - lémur.png
#   - bandera.png

# --------------------------SOLUCIÓN--------------------------
from PIL import Image

lemur = Image.open('lemur.png').convert('RGB')
flag_encrypted = Image.open('flag.png').convert('RGB')

assert lemur.size == flag_encrypted.size, "Error: Las imágenes tienen dimensiones diferentes"

resultado = Image.new('RGB', lemur.size)
for x in range(lemur.width):
    for y in range(lemur.height):
        r1, g1, b1 = lemur.getpixel((x, y))
        r2, g2, b2 = flag_encrypted.getpixel((x, y))
        resultado.putpixel((x, y), (r1 ^ r2, g1 ^ g2, b1 ^ b2))

resultado.save('bandera_descifrada.png')
resultado.show()