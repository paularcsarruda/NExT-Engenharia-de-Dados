#=========================================================
# Exercicio 01
#=========================================================
def eh_positivo(numero):
    return numero >= 0

valor = int(input("Digite um número inteiro: "))

if eh_positivo(valor):
    print("Positivo")
else:
    print("Negativo")

#=========================================================
# Exercicio 02
#=========================================================
def multiplicar_lista(lista, multiplicador):
    for numero in lista:
        print(numero * multiplicador)

numeros = [1, 2, 3, 4, 5]

valor = int(input("Digite o multiplicador: "))

multiplicar_lista(numeros, valor)

#=========================================================
# Exercicio 03
#=========================================================
def buscar_nome(lista, nome):
    return nome in lista

nomes = ["Ana", "Carlos", "Maria", "João", "Pedro"]

nome_procurado = input("Digite um nome: ")

if buscar_nome(nomes, nome_procurado):
    print("Nome encontrado.")
else:
    print("Nome não encontrado.")

#=========================================================
# Exercicio 04
#=========================================================
def celsius_para_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_para_celsius(f):
    return 5 * ((f - 32) / 9)

tipo = input("Deseja informar Celsius (C) ou Fahrenheit (F)? ").upper()

temperatura = float(input("Digite a temperatura: "))

if tipo == "C":
    print(f"{celsius_para_fahrenheit(temperatura):.2f} °F")
elif tipo == "F":
    print(f"{fahrenheit_para_celsius(temperatura):.2f} °C")
else:
    print("Opção inválida.")

#=========================================================
# Exercicio 05
#=========================================================
def ler_numeros():
    numeros = []

    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)

    return numeros

def exibir_invertido(lista):
    for i in range(len(lista) - 1, -1, -1):
        print(lista[i])

numeros = ler_numeros()
exibir_invertido(numeros)

#=========================================================
# Exercicio 06
#=========================================================
def inverter_lista(lista):
    for i in range(len(lista) - 1, -1, -1):
        print(lista[i])

numeros = [10, 20, 30, 40, 50]

inverter_lista(numeros)

#=========================================================
# Exercicio 07
#=========================================================