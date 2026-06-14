# Exercicio votação
#==============================
votos = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice', 'Charlie']
candidatos = set(votos)
print(candidatos)

for candidato in candidatos:
    print(candidato, votos.count(candidato))