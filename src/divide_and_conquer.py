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

# Definición de la función find_maximum_subarray.
def find_maximum_subarray(nums):

    # Caso base en el que si el arreglo tiene un solo elemento, entonces se retorna ese elemento.
    if (len(nums) == 1):

        # Se retorna el primer elemento del arreglo.
        return nums[0]

    # Caso inductivo en el que se divide el arreglo en dos subarreglos y se llama recursivamente a la función.
    else:

        # Cálculo del medio del arreglo y sus dos mitades.
        midpoint = (len(nums) // 2)
        left_subarray = nums[: midpoint]
        right_subarray = nums[midpoint :]

        # Se llama recursivamente a la función para cada mitad del arreglo.
        left_sum = find_maximum_subarray(left_subarray)
        right_sum = find_maximum_subarray(right_subarray)

        # La función find_crossing_subarray encuentra el subarreglo de mayor suma que cruza los dos subarreglos.
        crossing_sum = find_crossing_subarray(left_subarray, right_subarray)

        # Retorno del máximo entre las tres sumas encontradas.
        return max(left_sum, right_sum, crossing_sum)

# Definición de la función find_crossing_subarray.
def find_crossing_subarray(left_subarray, right_subarray):

    # Instancia inicial de left_sum y current_sum.
    left_sum = float("-inf")
    current_sum = 0

    # Iteración sobre el arreglo de la izquierda y se va sumando cada elemento a current_sum.
    for i in range((len(left_subarray) - 1), -1, -1):
        current_sum += left_subarray[i]
        if (current_sum > left_sum):
            left_sum = current_sum

    # Instancia inicial de right_sum y current_sum.
    right_sum = float("-inf")
    current_sum = 0

    # Iteración sobre el arreglo de la derecha y se va sumando cada elemento a current_sum.
    for i in range(len(right_subarray)):
        current_sum += right_subarray[i]
        if (current_sum > right_sum):
            right_sum = current_sum

    # Retorno de la suma de los dos subarreglos.
    return (left_sum + right_sum)
