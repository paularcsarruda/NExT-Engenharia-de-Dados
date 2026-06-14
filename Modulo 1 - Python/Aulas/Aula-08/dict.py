dados = dict()
dados['bear'] = 'urso'

for i in range(5):
    chave, valor = input('Digite chave e valor separados por espaço: ').split()
    dados[chave] = valor

print(dados)
