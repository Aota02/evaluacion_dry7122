#!/bin/bash

# Archivo de texto con contenido de prueba
echo "Contenido de prueba" > archivo_prueba.txt

# Modificación de los permisos
chmod 744 archivo_prueba.txt

# Cambio de propietario
sudo chown root:root archivo_prueba.txt

# Mostrar resultado
ls -l archivo_prueba.txt
