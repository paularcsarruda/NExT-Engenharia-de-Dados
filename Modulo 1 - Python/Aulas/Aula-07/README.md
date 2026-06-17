# ⚠️ Tratamento de Exceções em Python

O tratamento de exceções é um mecanismo que permite lidar com erros de forma controlada durante a execução de um programa.

Em vez de encerrar abruptamente a aplicação quando ocorre um problema, podemos capturar o erro, informar o usuário e continuar a execução do programa quando apropriado.

## 📌 O que são Exceções?

Exceções são erros detectados durante a execução do código.

### Exemplo de erro

```python
numero = 10 / 0
```

Saída:

```text
ZeroDivisionError: division by zero
```

Sem tratamento, o programa será interrompido.

---

# 🚀 Bloco Try e Except

O bloco `try` permite testar um trecho de código que pode gerar erros.

O bloco `except` captura e trata a exceção.

```python
try:
    numero = 10 / 0
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
```

Saída:

```text
Não é possível dividir por zero.
```

---

# 🎯 Capturando Diferentes Exceções

É possível tratar vários tipos de erro.

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero

except ValueError:
    print("Digite apenas números.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")
```

---

# 📖 Capturando a Mensagem do Erro

Podemos armazenar a exceção em uma variável.

```python
try:
    numero = int("abc")

except ValueError as erro:
    print(f"Erro encontrado: {erro}")
```

Saída:

```text
Erro encontrado: invalid literal for int()
```

---

# 🔄 Bloco Else

O bloco `else` é executado quando nenhuma exceção ocorre.

```python
try:
    numero = int(input("Digite um número: "))

except ValueError:
    print("Valor inválido.")

else:
    print("Número digitado com sucesso.")
```

---

# 🧹 Bloco Finally

O bloco `finally` é executado sempre, independentemente de ocorrer erro ou não.

```python
try:
    arquivo = open("dados.txt")

except FileNotFoundError:
    print("Arquivo não encontrado.")

finally:
    print("Encerrando operação.")
```

Saída:

```text
Encerrando operação.
```

Esse bloco é muito utilizado para:

- Fechar arquivos
- Encerrar conexões com banco de dados
- Liberar recursos do sistema

---

# 📂 Exemplo Completo

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero

except ValueError:
    print("Digite apenas números.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")

else:
    print(f"Resultado: {resultado}")

finally:
    print("Programa finalizado.")
```

---

# ⚡ Exceção Genérica

Podemos capturar qualquer exceção usando `Exception`.

```python
try:
    x = int(input("Digite um número: "))

except Exception as erro:
    print(f"Erro: {erro}")
```

⚠️ Utilize essa abordagem com cautela, pois ela captura qualquer erro e pode dificultar a identificação de problemas específicos.

---

# 🛠️ Lançando Exceções Manualmente

Utilizamos a palavra-chave `raise` para gerar exceções personalizadas.

```python
idade = -5

if idade < 0:
    raise ValueError("A idade não pode ser negativa.")
```

Saída:

```text
ValueError: A idade não pode ser negativa.
```

---

# 🎨 Criando Exceções Personalizadas

Também é possível criar nossas próprias exceções.

```python
class SaldoInsuficienteError(Exception):
    pass

saldo = 100
saque = 200

if saque > saldo:
    raise SaldoInsuficienteError(
        "Saldo insuficiente para realizar o saque."
    )
```

---

# 📚 Exceções Mais Comuns em Python

| Exceção | Descrição |
|----------|------------|
| `ValueError` | Valor inválido |
| `TypeError` | Tipo de dado incorreto |
| `NameError` | Variável não definida |
| `IndexError` | Índice inexistente |
| `KeyError` | Chave inexistente |
| `ZeroDivisionError` | Divisão por zero |
| `FileNotFoundError` | Arquivo não encontrado |
| `ImportError` | Erro ao importar módulo |
| `AttributeError` | Atributo inexistente |
| `RuntimeError` | Erro de execução |

---

# 📚 Resumo

O tratamento de exceções permite criar aplicações mais robustas e confiáveis.

Principais recursos:

- `try` → Executa código que pode gerar erro.
- `except` → Captura e trata exceções.
- `else` → Executa quando não há erros.
- `finally` → Executa sempre.
- `raise` → Lança exceções manualmente.
- Exceções personalizadas → Permitem criar regras específicas para o sistema.

Dominar o tratamento de exceções é fundamental para desenvolver aplicações profissionais e evitar falhas inesperadas.

---
