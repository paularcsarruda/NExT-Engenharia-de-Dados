#=======================================
# ARQUIVOS
# uma das formas de armazenar dados é utilizando arquivos, eles podem ser de diversos 
# tipos, como .txt, .csv, .json, entre outros.
# para trabalhar com arquivos em Python, utilizamos a função open(), que recebe como 
# parâmetro o nome do arquivo e o modo de abertura (leitura, escrita, etc).
# o modo de abertura pode ser:
# 'r' - leitura (padrão)
# 'w' - escrita (sobrescreve o arquivo)
# 'a' - escrita (adiciona ao final do arquivo)
# 'x' - escrita (cria um novo arquivo, falha se o arquivo já existe)
# 'b' - modo binário (para arquivos não textuais)   
#=======================================

with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#========================================
arquivo = open ("exemplo.txt", "r", encoding="utf-8")
print(arquivo.readline()) # lê a próxima linha do arquivo

#========================================
for linha in arquivo.readlines(): # lê todas as linhas do arquivo e retorna uma lista
    print(linha.strip()) # strip() remove os espaços em branco no início e no final da linha - caracteres de tabulação


#========================================
# MODO WRITE (sobrescreve o arquivo)

# ao abrir um arquivo no modo 'w', se o arquivo já existir, ele será sobrescrito, ou seja, todo o conteúdo anterior será 
# apagado e substituído pelo novo conteúdo que você escrever.
# se o arquivo não existir, ele será criado.
# para evitar perder dados importantes, é recomendado verificar se o arquivo já existe antes de abrir no modo 'w', 
# ou usar o modo 'a' para adicionar ao final do arquivo sem apagar o conteúdo existente.
# para abrir um arquivo no modo 'w', basta usar a função open() com o segundo argumento como 'w':
# arquivo = open("exemplo.txt", "w", encoding="utf-8")
#=========================================
with open("Aula-06/exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Esta é uma nova linha.\n") # escreve uma nova linha no arquivo
    arquivo.write("Esta é outra linha.\n")

#========================================
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    for i in range(3):
        numero = input("Digite um número: ")
        arquivo.write(numero + "\n")
print("Números escritos no arquivo.")

#========================================
arquivo.close() # é importante fechar o arquivo após o uso para liberar recursos do sistema