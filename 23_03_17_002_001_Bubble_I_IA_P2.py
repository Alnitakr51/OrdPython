# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 08:15:15 2023

@author: Gadiel Jimenez
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
mi_lista = [3, 7, 1, 9, 2,10,45,32,34,64]
resultado = bubble_sort(mi_lista)
print(resultado)
