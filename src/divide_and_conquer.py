"""
Universidad del Valle de Guatemala
(CC3041) Análisis y Diseño de Algoritmos
Proyecto 2 - Divide and Conquer vs. Programación Dinámica
Grupo: Los 3otsitos

Miembros del grupo:
- Pedro Pablo Arriola Jiménez (20188)
- José Rodrigo Barrera García (20807)
- Oscar Fernando López Barrios (20679)
- Yong Bum Park (20117)
- Roberto Francisco Ríos Morales (20979)
- Santiago Taracena Puga (20017)

Archivo: divide_and_conquer.py
El presente archivo contiene las funciones find_maximum_subarray y
find_crossing_subarray, las cuales son las funciones que tienen como
objetivo solucionar el problema de encontrar el subarreglo de mayor
suma en un arreglo de números enteros mediante un algoritmo basado en
divide and conquer. El algoritmo divide el arreglo en dos subarreglos
de manera recursiva hasta que el tamaño de cada subarreglo sea 1, y
luego los une para encontrar el subarreglo de mayor suma que cruza
los dos subarreglos.
"""

def find_maximum_subarray(nums):
    if (len(nums) == 1):
        return nums[0]
    else:
        mid = (len(nums) // 2)
        left_subarray = nums[:mid]
        right_subarray = nums[mid:]

        left_sum = find_maximum_subarray(left_subarray)
        right_sum = find_maximum_subarray(right_subarray)
        crossing_sum = find_crossing_subarray(left_subarray, right_subarray)

        return max(left_sum, right_sum, crossing_sum)

def find_crossing_subarray(left_subarray, right_subarray):
    left_sum = float("-inf")
    current_sum = 0

    for i in range(len(left_subarray)-1, -1, -1):
        current_sum += left_subarray[i]
        if current_sum > left_sum:
            left_sum = current_sum

    right_sum = float("-inf")
    current_sum = 0

    for i in range(len(right_subarray)):
        current_sum += right_subarray[i]
        if current_sum > right_sum:
            right_sum = current_sum

    return left_sum + right_sum
