#==============================
# TUPLA, SET E DICIONÁRIO
#==============================

# TUPLAS
# coleção ordenada e imutável de elementos
#==============================
numeros = (1, 2, 3, 4, 5)
print(numeros)
print(numeros[0])
print(numeros[1:4])
print(len(numeros))
print(3 in numeros)
print(numeros.index(4))

# convertendo lista para tupla
#==========================
numbers = [1, 2, 3, 4, 5]
numbers_tuple = tuple(numbers)
print(numbers_tuple)

# SETS
# coleção não ordenada e mutável de elementos únicos
# não aceita elementos duplicados
#==============================
conjunto = {1, 2, 3, 4, 5}
print(conjunto)
conjunto.add(6)
conjunto.add(3)  # não será adicionado, pois já existe
conjunto.add('3')  # string '3' é diferente do número 3
print(conjunto)
conjunto.remove(3)
print(conjunto)
print(2 in conjunto)

# DICIONÁRIOS
# coleção de pares chave-valor
#==============================
dicionario = {'nome': 'Alice', 'idade': 30, 'cidade': 'São Paulo'}
print(dicionario)
print(dicionario['nome'])
print(dicionario.get('idade', 'Chave não encontrada')) # retorna None se a chave não existir
dicionario['profissao'] = 'Engenheira'
print(dicionario)
del dicionario['cidade']
dicionario.pop('idade')
print(dicionario)

#==============================
animais = {'cachorro': 'au au', 'gato': 'miau', 'vaca': 'muu'}
print(animais['cachorro'])
print(animais['gato'])
print(animais['vaca'])
