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

Parte de pruebas empiricas

Este mini programa solo sirve para medir los tiempos 
de ejecucion que se presentan en el documento de entrega.

"""

import timeit
import random
import divide_and_conquer as dac
import dynamic_programming as dp
import matplotlib.pyplot as plt
import pandas as pd
# import cProfile

# abrir un archivo csv para poder almacenar resultados
file = open('results.csv',mode='w')
file.write('id,size,dac_time,dp_time,array\n')

# inicializar tamano inicial, valores min y max en los arrays 
n = 10
min_val = -100
max_val = 100


# medir execution time 30 veces con arrays cada vez mas grandes
for i in range(1,31):
    # crear array aleatorio de tamano n
    array = [random.randint(min_val, max_val) for i in range(n)]

    # medir el tiempo de divide_and_conquer
    dac_execution_time = timeit.timeit(stmt=f'''
import divide_and_conquer as dac
dac.find_maximum_subarray({array})
    ''',
    setup='import divide_and_conquer',
    number=1000)
    # cProfile.run(dac.find_maximum_subarray(array))

    # medir el tiempo de dynamic_programming
    dp_execution_time = timeit.timeit(stmt=f'''
import dynamic_programming as dp
dp.find_maximum_subarray({array})
    ''',
    setup='import dynamic_programming',
    number=1000)


    # registrar resultados
    array_str = '"' + str(array) + '"'
    file.write(f"{i},{n},{dac_execution_time},{dp_execution_time},{array_str}\n")

    # aumentar el tamano del array
    n = n + 10


# output
file.close()

# Read in the CSV file using pandas
df = pd.read_csv('results.csv')

# Extract the three columns you want to plot
x = df['size']
y1 = df['dac_time']
y2 = df['dp_time']

# Plot the data as lines
plt.plot(x, y1, label='dac')
plt.plot(x, y2, label='dp')

# Add labels and title to the plot
plt.xlabel('size')
plt.ylabel('time')
plt.title('Time vs size')

# Add legend to the plot
plt.legend()

# Show the plot
plt.show()
