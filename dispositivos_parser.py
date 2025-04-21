# dispositivos_parser.py

import json

# Abrir el archivo JSON
with open("dispositivos.json", "r") as archivo:
    dispositivos_data = json.load(archivo)

# Mostrar los datos de forma clara
print("\n--- Lista de Dispositivos de Red ---\n")

for dispositivo in dispositivos_data["dispositivos"]:
    print(f"Nombre:     {dispositivo['nombre']}")
    print(f"Dirección IP: {dispositivo['ip']}")
    print(f"Estado:     {dispositivo['estado']}")
    print("-" * 30)
