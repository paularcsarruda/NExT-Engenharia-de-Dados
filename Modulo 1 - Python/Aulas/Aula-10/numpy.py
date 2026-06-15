#================================
# NUMPY
'''
O NumPy é uma biblioteca fundamental para a computação científica em Python. 
Ele fornece suporte para arrays multidimensionais e uma coleção de funções 
matemáticas para operar com esses arrays de forma eficiente. O NumPy é amplamente 
utilizado em áreas como análise de dados, aprendizado de máquina, processamento de 
imagens e muito mais.
'''
#================================

import numpy as np

# Criando um array a partir de uma lista
lista = [1, 2, 3, 4, 5]
array = np.array(lista)
print("Array criado a partir de uma lista:")
print(array)

# Criando um array multidimensional
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray multidimensional (matriz):")
print(matriz)   