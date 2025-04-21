# verificación_puerto.py

try:
    puerto = int(input("Ingrese un número de puerto: "))

    if 0 <= puerto <= 1023:
        print("Puerto bien conocido")
    elif 1024 <= puerto <= 49151:
        print("Puerto registrado")
    elif 49152 <= puerto <= 65535:
        print("Puerto dinámico o privado")
    else:
        print("No corresponde a un puerto válido")
except ValueError:
    print("Debes ingresar un número entero válido.")
