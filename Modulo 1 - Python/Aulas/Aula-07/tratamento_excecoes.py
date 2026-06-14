#=====================================
# PIPELINE ETL
# extract, transform and load
#=====================================
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

try:
    resultado = num1 / num2
    print(f'O resultado da divisão é: {resultado}')
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

#=====================================
# TRATAMENTO DE EXCEÇÕES
#=====================================
try:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    resultado = num1 / num2
    print(f'O resultado da divisão é: {resultado}')
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

#=====================================
# TRATAMENTO DE EXCEÇÕES COM FINALLY
#=====================================
try:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    resultado = num1 / num2
    print(f'O resultado da divisão é: {resultado}')
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except Exception:
    print(f"Algo de errado não está certo.")
finally:
    print("Fim do programa.")

#=====================================
# TRATAMENTO DE EXCEÇÕES COM ELSE
#=====================================
try:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    resultado = num1 / num2
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
else:
    print(f'O resultado da divisão é: {resultado}')
finally:
    print("Fim do programa.")

