#=====================================================
# MÓDULOS E PACOTES
''''
Módulo: arquivo Python que contém definições e instruções
Pacote: coleção de módulos organizados em diretórios
'''
#=====================================================

import math # importa o módulo math inteiro, pode ser importado como math ou math as m
from math import sqrt, pi, factorial
import random as rd

print(math.sqrt(16))
print(pi)
print(factorial(5))
print(rd.choice([1, 2, 3, 4, 5]))
print(math.pow(2, 3)) # 2 elevado a 3

#=====================================================
# DATETIME
# O módulo datetime fornece classes para manipular datas e horas
#======================================================
from datetime import datetime, timedelta

print(datetime.now()) # data e hora atual
print(datetime.now().date()) # data atual
print(datetime.now().time()) # hora atual
print(datetime.now().year) # ano atual
print(datetime.now().month) # mês atual

amanha = datetime.now() + timedelta(days=1) # data de amanhã
print(amanha)

dta_formatada = datetime.now().strftime('%d/%m/%Y %H:%M:%S') # formata a data e hora
print(dta_formatada)

#=====================================================
# OS
# O módulo os fornece funções para interagir com o sistema operacional
#======================================================
import os   

print(os.getcwd()) # diretório atual
os.mkdir('novo_diretorio') # cria um novo diretório
os.rename('novo_diretorio', 'diretorio_renomeado') # renomeia o diretório
os.rmdir('diretorio_renomeado') # remove o diretório