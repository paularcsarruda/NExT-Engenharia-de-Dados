import csv
from csv import DictReader

with open('Modulo 1 - Python/Aulas/Aula-09/dados.csv', 'r') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    for linha in leitor_csv:
        print(linha)
        print(linha['Cidade']) # Acessando a coluna 'cidade' usando o nome da coluna