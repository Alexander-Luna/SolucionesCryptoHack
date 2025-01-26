import sys

if sys.version_info.major == 2:
    print("No puedes ejecutar en Python2 por favor usa Python3")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Su bandera es:")
print("".join(chr(o ^ 0x32) for o in ords))
