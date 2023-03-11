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

Archivo: dynamic_programming.py
El presente archivo contiene la función find_maximum_subarray, la cual
es la función que tiene como objetivo solucionar el problema de encontrar
el subarreglo de mayor suma en un arreglo de números enteros mediante un
algoritmo basado en programación dinámica. El algoritmo itera sobre el
arreglo y va guardando la suma máxima hasta el momento en una variable
llamada current_sum. Si current_sum es menor que 0, entonces se reinicia
a 0, ya que no hay ningún beneficio en sumarle un número negativo a la
suma actual. Si current_sum es mayor que 0, entonces se suma el número
actual a current_sum. Finalmente, se compara current_sum con la suma
máxima hasta el momento, y si current_sum es mayor, entonces se actualiza
la suma máxima hasta el momento.
"""

def find_maximum_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum
