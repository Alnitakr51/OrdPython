# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 08:16:49 2023

@author: Gadiel Jimenez
"""

def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r 

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

mi_lista = [3, 7, 1, 9, 12,22,34,73,13,2,74,87,43]
resultado = heap_sort(mi_lista)
print(resultado) 

