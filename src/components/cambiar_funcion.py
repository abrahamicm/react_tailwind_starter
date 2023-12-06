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

        # Buscar el patrón en el contenido del archivo
        patron = r'export\s+default\s+function\s+Example'
        coincidencias = re.findall(patron, contenido)

        # Si hay coincidencias, reemplazar 'Example' por el nombre del archivo sin extensión
        if coincidencias:
            nuevo_contenido = re.sub(patron, f'export default function {archivo[:-4]}', contenido)

            # Escribir el nuevo contenido de vuelta al archivo
            with open(os.path.join(directorio_actual, archivo), 'w', encoding='utf-8') as f:
                f.write(nuevo_contenido)
