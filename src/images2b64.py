#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script para codificar todas las imagenes de un directorio a base64
1. Obtener un list de toas las imagenes
2. comprobar que sean archivos y no directorios
3. Codificar a base64
4. Guardar en un csv nombre de la imagen y su string en base64
"""

import os
import base64
import csv

files = os.listdir(".")
for item in files:
    if os.path.isfile(item):
        with open(item, "rb") as image, open('import-images.csv', 'w') as archivo:
            encode_image = base64.b64encode(image.read())
            encode_image = encode_image.decode("ascii")
            writer = csv.writer(archivo)
            writer.writerow([item, encode_image])
    else:
        pass
    
with open('import-images.csv', 'r') as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
