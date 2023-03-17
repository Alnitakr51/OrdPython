# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 08:16:30 2023

@author: Gadiel Jimenez
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
mi_lista = [3, 7, 1, 9, 2,25,84,23,12,54,13]
resultado = quick_sort(mi_lista)
print(resultado)
