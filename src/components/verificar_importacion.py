import os
import re

# Obtener el directorio actual del script
directorio_actual = os.getcwd()

# Obtener la lista de archivos en el directorio actual
archivos = os.listdir(directorio_actual)

# Iterar sobre cada archivo en el directorio
for archivo in archivos:
    if archivo.endswith('.tsx'):
        try:
            # Leer el contenido del archivo
            with open(os.path.join(directorio_actual, archivo), 'r', encoding='utf-8') as f:
                contenido = f.read()
        except UnicodeDecodeError:
            print(f"Error al leer el archivo {archivo}. Se omite.")
            continue

        # Verificar si la importación de React está presente
        if 'import React from "react";' not in contenido:
            # Agregar la importación al inicio del archivo
            nuevo_contenido = 'import React from "react";\n' + contenido

            # Escribir el nuevo contenido de vuelta al archivo
            with open(os.path.join(directorio_actual, archivo), 'w', encoding='utf-8') as f:
                f.write(nuevo_contenido)
