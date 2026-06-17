# 📂 Manipulação de Arquivos em Python

## 📌 O que é Manipulação de Arquivos?

Manipulação de arquivos consiste em interagir com dados armazenados no sistema operacional.

Com Python podemos:

- Ler arquivos existentes
- Criar novos arquivos
- Escrever informações em arquivos
- Adicionar conteúdo sem apagar dados anteriores
- Trabalhar com arquivos de texto e binários
- Gerenciar diretórios e pastas

---

# 🛠️ Modos de Abertura

| Modo | Descrição |
|--------|------------|
| `r` | Leitura |
| `w` | Escrita (sobrescreve o arquivo) |
| `a` | Adiciona conteúdo ao final |
| `x` | Cria um novo arquivo |
| `rb` | Leitura binária |
| `wb` | Escrita binária |
| `r+` | Leitura e escrita |

---

# 📖 Abrindo Arquivos

A função `open()` é utilizada para abrir arquivos.

```python
arquivo = open("dados.txt")
```

Sintaxe:

```python
open(nome_arquivo, modo)
```

Exemplo:

```python
arquivo = open("dados.txt", "r")
```

---

# 📥 Lendo Arquivos

## Ler todo o conteúdo

```python
arquivo = open("dados.txt", "r")

conteudo = arquivo.read()

print(conteudo)

arquivo.close()
```

---

## Ler uma linha

```python
arquivo = open("dados.txt", "r")

linha = arquivo.readline()

print(linha)

arquivo.close()
```

---

## Ler todas as linhas

```python
arquivo = open("dados.txt", "r")

linhas = arquivo.readlines()

print(linhas)

arquivo.close()
```

---

# ✍️ Escrevendo em Arquivos

## Criando ou sobrescrevendo um arquivo

```python
arquivo = open("dados.txt", "w")

arquivo.write("Olá, Python!")

arquivo.close()
```

⚠️ O modo `w` apaga o conteúdo anterior do arquivo.

---

# ➕ Adicionando Conteúdo

O modo `a` adiciona informações ao final do arquivo.

```python
arquivo = open("dados.txt", "a")

arquivo.write("\nNova linha adicionada.")

arquivo.close()
```

---

# 🧹 Fechando Arquivos

Após utilizar um arquivo, ele deve ser fechado.

```python
arquivo.close()
```

Isso libera recursos do sistema operacional.

---

# ✅ Utilizando Context Manager (with)

A forma recomendada de trabalhar com arquivos é utilizando `with`.

O arquivo é fechado automaticamente, mesmo em caso de erro.

```python
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
```

---

# 📄 Escrevendo com With

```python
with open("dados.txt", "w") as arquivo:
    arquivo.write("Texto salvo com sucesso.")
```

---

# 🔄 Percorrendo Arquivos

```python
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

---

# 📋 Arquivos CSV

CSV (Comma-Separated Values) é um formato amplamente utilizado para armazenamento de dados tabulares.

## Escrevendo CSV

```python
import csv

with open("usuarios.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(["Nome", "Idade"])
    escritor.writerow(["Ana", 25])
    escritor.writerow(["Carlos", 30])
```

---

## Lendo CSV

```python
import csv

with open("usuarios.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)
```

---

# 📑 Trabalhando com JSON

JSON é um dos formatos mais utilizados para troca de dados.

## Gravando JSON

```python
import json

dados = {
    "nome": "Ana",
    "idade": 25
}

with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)
```

---

## Lendo JSON

```python
import json

with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)

print(dados)
```

---

# 🗂️ Manipulando Diretórios com os

O módulo `os` permite interagir com o sistema operacional.

## Obter diretório atual

```python
import os

print(os.getcwd())
```

---

## Criar pasta

```python
os.mkdir("nova_pasta")
```

---

## Remover pasta

```python
os.rmdir("nova_pasta")
```

---

## Listar arquivos

```python
print(os.listdir())
```

---

# 📚 Resumo

| Operação | Método |
|------------|------------|
| Abrir arquivo | `open()` |
| Ler conteúdo | `read()` |
| Ler linha | `readline()` |
| Ler linhas | `readlines()` |
| Escrever | `write()` |
| Fechar | `close()` |
| Context Manager | `with open()` |
| Trabalhar com JSON | `json` |
| Trabalhar com CSV | `csv` |
| Manipular diretórios | `os` |
| Manipular caminhos | `pathlib` |

---
