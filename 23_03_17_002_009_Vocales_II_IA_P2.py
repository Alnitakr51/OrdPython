# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 08:48:38 2023

@author: Gadiel Jimenez
"""

def contar_vocales(palabra):
    vocales = "aeiou"
    count = 0
    for letra in palabra:
        if letra.lower() in vocales:
            count += 1
    return count

palabras = ["carro", "termo", "gorra", "flor", "chocolate", "playa", "xilófono"]
palabras.sort(key=contar_vocales)
print(palabras)
