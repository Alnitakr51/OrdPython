# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 08:15:32 2023

@author: Gadiel Jimenez
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
mi_lista = [3, 7, 1, 9,4,5,12,76,8,45,2]
resultado = selection_sort(mi_lista)
print(resultado)
