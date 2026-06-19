# SQL

## Aula 1: Introdução a Banco de Dados

**Professor: Ricardo Teixeira**

---

# 1. Fundamentos

## O que é um Banco de Dados (BD)?

Um **Banco de Dados (BD)** é uma coleção organizada de informações armazenadas eletronicamente, permitindo consulta, atualização e gerenciamento eficiente dos dados.

### Exemplos

* Cadastro de clientes de uma loja.
* Sistema acadêmico de uma universidade.
* Aplicativos de redes sociais.
* Sistemas bancários.

---

## O que é um SGBD?

Um **Sistema Gerenciador de Banco de Dados (SGBD)** é o software responsável por criar, acessar, manipular e proteger os dados armazenados em um banco de dados.

### Exemplos de SGBDs

* MySQL
* PostgreSQL
* Oracle Database
* Microsoft SQL Server

### Principais Funções do SGBD

* Armazenar e organizar dados.
* Localizar registros rapidamente.
* Controlar acesso e permissões dos usuários.
* Garantir a integridade dos dados.
* Controlar concorrência (evitar conflitos entre usuários).
* Realizar backups e recuperação de dados.

---

## Propriedades ACID

As transações em um SGBD seguem as propriedades **ACID**, garantindo confiabilidade.

### Atomicidade (Atomicity)

Uma transação é executada completamente ou não é executada.

### Consistência (Consistency)

Os dados permanecem válidos antes e após a transação.

### Isolamento (Isolation)

Transações simultâneas não interferem umas nas outras.

### Durabilidade (Durability)

Após a confirmação da transação (*commit*), os dados permanecem gravados mesmo em caso de falha.

---

# Banco de Dados Relacional e Não Relacional

## Banco de Dados Relacional (SQL)

Os dados são organizados em **tabelas**, compostas por linhas e colunas.

### Características

* Estrutura rígida.
* Relacionamentos entre tabelas.
* Uso de chaves primárias (PK) e estrangeiras (FK).
* Utilização da linguagem SQL.

### Exemplo

| ID | Nome | Curso |
| -- | ---- | ----- |
| 1  | Ana  | ADS   |
| 2  | João | SI    |

---

## Banco de Dados Não Relacional (NoSQL)

Os dados não precisam seguir o modelo de tabelas.

### Características

* Estrutura flexível.
* Alta escalabilidade.
* Ideal para grandes volumes de dados.

### Tipos

* Documento
* Chave-valor
* Colunar
* Grafo

### Exemplo JSON

```json
{
  "id": 1,
  "nome": "Ana",
  "curso": "ADS"
}
```

---

# Modelos de Organização de Dados

## Modelo Hierárquico

* Estrutura em árvore.
* Cada registro possui apenas um pai.

## Modelo em Rede

* Permite múltiplos relacionamentos entre registros.
* Mais flexível que o modelo hierárquico.

## Modelo Relacional

* Baseado em tabelas.
* Atualmente é o modelo mais utilizado.
* Utiliza SQL para manipulação dos dados.

---

# 2. Níveis e Atores da Modelagem

O desenvolvimento de um banco de dados normalmente segue quatro fases.

## Fase 1: Mini-Mundo

### Objetivo

Entender o negócio e os problemas do cliente.

### Características

* Levantamento de requisitos.
* Não depende de um SGBD específico.
* Identificação das informações importantes.

### Ferramentas

* Entrevistas
* Questionários
* BRModelo

---

## Fase 2: Modelo Conceitual

### Objetivo

Representar graficamente as informações do negócio.

### Elementos

* Entidades
* Atributos
* Relacionamentos

### Exemplo

```text
Aluno ---- Matrícula ---- Curso
```

---

## Fase 3: Modelo Lógico

### Objetivo

Transformar o modelo conceitual em tabelas.

### Definições

* Tabelas
* Campos
* Chaves Primárias (PK)
* Chaves Estrangeiras (FK)
* Regras de integridade

---

## Fase 4: Modelo Físico

### Objetivo

Implementar o banco de dados no SGBD escolhido.

### Resultado

Scripts SQL executados diretamente no banco.

### Exemplo

```sql
CREATE TABLE aluno (
    id INT PRIMARY KEY,
    nome VARCHAR(100)
);
```

---

# 3. Modelagem Entidade-Relacionamento (ER) - Conceitual

A modelagem ER é uma técnica utilizada para representar graficamente os dados de um sistema antes da implementação.

## Componentes

### Entidade (os substantivos)

Representa um objeto do mundo real.

**Exemplos:**

* Aluno
* Professor
* Curso

### Atributo (os adjetivos)

Características de uma entidade.

**Exemplos:**

* Nome
* CPF
* Data de Nascimento

### Atributo Chave (identificador)

A propriedade única que não se repete sob hipotese alguma.

**Exemplos:**

* CPF
* ID_produto

### Relacionamento

Associação entre entidades.

**Exemplo:**

```text
Aluno realiza Matrícula
```

### Cardinalidade

Define quantas ocorrências de uma entidade podem se relacionar com outra.

#### 1:1

Um para um.

#### 1:N

Um para muitos.

#### N:N

Muitos para muitos.

---

# 4. Prática Guiada

## Fluxo Completo de Desenvolvimento

```text
Mini-Mundo
     ↓
Modelo Conceitual
     ↓
Modelo Lógico
     ↓
Modelo Físico
     ↓
Implementação SQL
```

---

# Resumo da Aula

* Banco de Dados armazena informações de forma organizada.
* SGBDs gerenciam e protegem os dados.
* Transações seguem as propriedades ACID.
* Bancos relacionais utilizam tabelas e SQL.
* Bancos não relacionais oferecem maior flexibilidade.
* A modelagem passa pelas etapas:

  * Mini-Mundo
  * Modelo Conceitual
  * Modelo Lógico
  * Modelo Físico
* A modelagem ER utiliza entidades, atributos e relacionamentos para representar o sistema antes da implementação.
