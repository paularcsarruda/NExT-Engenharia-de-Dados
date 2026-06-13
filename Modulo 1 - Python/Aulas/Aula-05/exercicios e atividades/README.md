# NExT 26.1 | Fundamentos de Python Aplicado a Dados

![CESAR School](/cesar_school.png)

## Aula 05 - Funções

## Função com funções

Funções internas ou funções aninhadas, são funções definidas dentro de outras funções.

Podem ser usadas para esconder um recurso de acesso externo ou para criação de funções auxiliares que só funcionam em determinado contexto.

Mais sobre Inner Functions [aqui](https://realpython.com/inner-functions-what-are-they-good-for/).

## 🐝 Beecrowd

[3475 - Conversor](https://judge.beecrowd.com/pt/problems/view/3475)

[1099 - Soma de Ímpares Consecutivos II](https://judge.beecrowd.com/pt/problems/view/1099)

[1151 - Fibonacci Fácil](https://judge.beecrowd.com/pt/problems/view/1151)

## 🧱 Exercícios Fundamentais

### [Exercício 01]

Crie um programa que receba um valor inteiro e avalie se ele é positivo ou negativo. Essa avaliação deve ocorrer dentro de uma função que retorna um valor booleano.

### [Exercício 02]

Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba todos os valores multiplicados por um valor inserido pelo usuário.

### [Exercício 03]

Crie um programa que possua uma lista de nomes. Peça que o usuário insira um nome que será buscado nesta lista. A busca deve ser implementada em uma função que retorna os valores lógicos verdadeiro, caso o nome seja encontrado na lista ou falso, caso contrário.

### [Exercício 04]

Implemente um programa que possa receber do usuário a temperatura em graus Celsius ou Fahrenheit. Antes de receber a temperatura, pergunte ao usuário se ele deseja inserir em Celsius ou em Fahrenheit. Se a entrada for em graus Celsius, o programa deverá retornar a temperatura em Fahrenheit. Se a entrada for em Fahrenheit, o programa deverá retornar a temperatura em Celsius.

$$ °C = 5 \times ((°F-32) / 9) $$
$$ °F = (°C \times 9 / 5) + 32 $$

### [Exercício 05]

Crie um programa que receba do usuário 5 números inteiros e os exiba na tela na ordem contrária a que foi inserido. A leitura dos números deve ser feita em uma função e a exibição dos valores em ordem contrária deve ocorrer em outra função.

### [Exercício 06]

Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba todos os seus valores em ordem invertida.
Obs.: Sem usar `invert` ou o fatiador com passo `-1`.

## 🤿 Exercícios de Aprofundamento

⚠️ Alguns desses exercícios exigem conhecimentos ainda não apresentados no curso!

### [Exercício 07]

Faça um programa para imprimir:

  ```txt
  1
  2   2
  3   3   3
  .....
  n   n   n   n   n   n  ... n
  ```

### [Exercício 08]

Faça um programa para imprimir:

  ```txt
  1
  1   2
  1   2   3
  .....
  1   2   3   ...  n
  ```

### [Exercício 09]

Faça uma função que receba um valor inteiro e positivo e calcule o seu fatorial.

### [Exercício 10]

Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

### [Exercício 11]

Um palíndromo é uma palavra que se soletra da mesma forma nos dois sentidos, como “osso” e “reviver”. Escreva um função que dado uma plavra verifique se ela é palindromo.

### [Exercício 12]

Construa uma função que receba uma string como parâmetro e devolva outra string com os caracteres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

💡 Pesquise sobre o módulo `random`
