#================================
# FUNÇÕES
#================================


# Função sem parâmetros
def saudacao():
    print("Olá! Seja bem-vindo(a) ao NExT!")
saudacao()

# Função com parâmetros
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a) ao NExT!")

nome = input("Digite seu nome: ")
saudacao(nome)

# Função com mais de um parâmetro
def media (num1, num2):
    print(num1 + num2 / 2)

media(10, 32)

# Função com argumentos posicionais
def pedido(*toppings, tamanho='M'):
    print('*' * 10)
    for item in toppings:
        print(f"- {item}")
    print(f"Tamanho: {tamanho}")
    print('*' * 10)
    
pedido('acai', 'granola', 'banana', tamanho='P')
pedido('acai','granola', 'leite em pó', 'nutela', tamanho='G')
pedido('acai','granola', 'leite em pó', 'nutela', 'sucrilhos', 'paçoca', tamanho='M')


# Exemplo de função para verificar velocidade

def velocidade (distancia, tempo):
    return distancia / tempo

velocidade = velocidade(100, 2)

if velocidade > 60:
    print("Velocidade acima do limite permitido.")
else:
    print("Velocidade dentro do limite permitido.")

# Função para montar nome completo
def nome_completo(nome, sobrenome):
    nome = nome.capitalize()
    sobrenome = sobrenome.capitalize()
    return f"{nome} {sobrenome}"

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print(nome_completo(nome, sobrenome))

#=========================================================
def nome_completo(nome, sobrenome):
    nome = nome.capitalize()
    sobrenome = sobrenome.capitalize()

    return f"{nome} {sobrenome}"

nomes = []

for i in range(5):
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")

    nome_formatado = nome_completo(nome, sobrenome)
    nomes.append(nome_formatado)

print(nomes)
