# 🐍 Estruturas de Dados em Python

As estruturas de dados são formas de organizar, armazenar e manipular informações dentro de um programa. Python oferece diversas estruturas nativas que tornam o desenvolvimento mais simples, eficiente e legível.

## 📌 O que são Estruturas de Dados?

Estruturas de dados são maneiras de organizar informações para facilitar operações como:

- Armazenamento
- Busca
- Inserção
- Remoção
- Ordenação
- Manipulação de dados

As principais estruturas de dados nativas do Python são:

- Listas (`list`)
- Tuplas (`tuple`)
- Conjuntos (`set`)
- Dicionários (`dict`)

---

# 📋 Listas (Lists)

Listas são coleções ordenadas e mutáveis.

Isso significa que os elementos possuem posição definida e podem ser alterados após a criação.

## Criando uma Lista

```python
frutas = ["Maçã", "Banana", "Laranja"]

print(frutas)
```

---

# 📍 Tuplas (Tuples)

Tuplas são coleções ordenadas e imutáveis.

Depois de criadas, seus valores não podem ser modificados.

## Criando uma Tupla

```python
cores = ("Azul", "Verde", "Vermelho")
```

## Vantagens das Tuplas

- Mais rápidas que listas em alguns cenários.
- Menor consumo de memória.
- Garantem que os dados não sejam alterados acidentalmente.

---

# 🎯 Conjuntos (Sets)

Sets são coleções não ordenadas e sem elementos duplicados.

## Criando um Set

```python
numeros = {1, 2, 3, 4, 5}
```

---

# 📖 Dicionários (Dictionaries)

Dicionários armazenam dados em pares chave-valor.

São uma das estruturas mais utilizadas em Python.

## Criando um Dicionário

```python
pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "Recife"
}
```

# 🔍 Comparação das Estruturas

| Estrutura | Ordenada | Mutável | Permite Duplicados |
|------------|------------|------------|------------|
| List | ✅ | ✅ | ✅ |
| Tuple | ✅ | ❌ | ✅ |
| Set | ❌ | ✅ | ❌ |
| Dict | ✅* | ✅ | Chaves: ❌ |

---

# 📊 Estruturas Aninhadas

É possível combinar estruturas de dados.

## Lista de Dicionários

```python
alunos = [
    {"nome": "Ana", "nota": 9},
    {"nome": "Carlos", "nota": 8},
    {"nome": "Maria", "nota": 10}
]
```

## Dicionário com Listas

```python
curso = {
    "Python": ["Ana", "Carlos", "Maria"]
}
```

---

# 📚 Resumo

| Estrutura | Melhor Uso |
|------------|------------|
| List | Coleções que mudam frequentemente |
| Tuple | Dados fixos |
| Set | Valores únicos |
| Dict | Associação chave-valor |

