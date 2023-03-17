# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 08:15:42 2023

@author: Gadiel Jimenez
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
mi_lista = [3, 7, 1, 9, 2,32,345,76,45,7,76]
resultado = insertion_sort(mi_lista)
print(resultado)
