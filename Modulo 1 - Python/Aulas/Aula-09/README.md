# 📦 Módulos e Pacotes em Python

Módulos e pacotes são recursos fundamentais do Python para organizar código, reutilizar funcionalidades e estruturar projetos de forma profissional.

Eles permitem dividir aplicações grandes em partes menores e mais fáceis de manter, evitando arquivos gigantes e código duplicado.

## 📌 O que é um Módulo?

Um módulo é simplesmente um arquivo Python (`.py`) que contém funções, classes, variáveis ou qualquer código reutilizável.

### Exemplo de módulo

Arquivo: `calculadora.py`

```python
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b
```

## 📥 Importando um Módulo

```python
import calculadora

resultado = calculadora.soma(10, 5)

print(resultado)
```

### Importando funções específicas

```python
from calculadora import soma

print(soma(10, 5))
```

### Importando com apelido

```python
import calculadora as calc

print(calc.soma(10, 5))
```

## 📌 O que é um Pacote?

Um pacote é uma pasta que agrupa vários módulos relacionados.

Essa estrutura facilita a organização de projetos maiores.

### Estrutura de exemplo

```text
meu_projeto/
│
├── main.py
│
└── matematica/
    ├── __init__.py
    ├── operacoes.py
    └── estatistica.py
```

## 📂 Arquivo `__init__.py`

O arquivo `__init__.py` identifica um diretório como um pacote Python.

Embora seja opcional em versões mais recentes do Python, ainda é amplamente utilizado para:

- Inicializar pacotes
- Definir importações padrão
- Organizar APIs públicas

Exemplo:

```python
from .operacoes import soma
```

## 📥 Importando Módulos de um Pacote

Arquivo: `operacoes.py`

```python
def soma(a, b):
    return a + b
```

Arquivo: `main.py`

```python
from matematica.operacoes import soma

print(soma(5, 3))
```

## 🏗️ Criando Seu Próprio Pacote

Estrutura:

```text
meu_pacote/
│
├── __init__.py
├── calculos.py
└── utilidades.py
```

Arquivo `calculos.py`

```python
def multiplicar(a, b):
    return a * b
```

Uso:

```python
from meu_pacote.calculos import multiplicar

print(multiplicar(4, 5))
```

## 📋 Boas Práticas

- Utilize nomes claros para módulos e pacotes.
- Evite arquivos muito grandes.
- Organize funcionalidades relacionadas em pacotes.
- Evite importações desnecessárias.
- Prefira importações explícitas.
- Siga as recomendações da PEP 8.

## 🎯 Quando Usar Módulos?

Utilize módulos quando:

- O código puder ser reutilizado.
- Houver muitas funções relacionadas.
- Desejar separar responsabilidades.

## 🎯 Quando Usar Pacotes?

Utilize pacotes quando:

- O projeto crescer.
- Existirem vários módulos relacionados.
- For necessário organizar funcionalidades por categorias.

## 📚 Exemplo de Estrutura Profissional

```text
projeto/
│
├── main.py
├── requirements.txt
│
├── models/
├── services/
├── utils/
├── database/
└── tests/
```

Essa organização é comum em aplicações web, APIs, automações e projetos de Ciência de Dados.

Este projeto está licenciado sob a licença MIT.

---

⭐ Se este repositório foi útil para você, considere deixar uma estrela.
