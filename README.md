

## ❓ Problema

Um `bracket` é considerado qualquer um dos seguintes caracteres: 
* Colchetes: [ ou ];
* Parênteses: ( ou );
* Chaves: { ou }.

Dois `brackets` são considerados um par combinado se um `bracket` de abertura (ou seja, `(`, `[`, ou `{`) ocorre à esquerda de um `bracket` de fechamento (ou seja,`)`,`]` ou`}`) do mesmo tipo. Existem três tipos de pares de `brackets`: `[]`, `{}` e `()`.

Um par de brackets correspondente não é balanceado se o conjunto de bracket que ele inclui não for igual. Por exemplo, {[(])} não é balanceado porque o conteúdo entre { e } não é balanceado. O par de colchetes inclui um único parêntese de abertura não balanceado, (, e o par de parênteses inclui um único colchete de fechamento não balanceado,].

Por essa lógica, dizemos que uma sequência de brackets é equilibrada se as seguintes condições forem atendidas:

* Ele contém um par de `bracket`.

* O subconjunto de `brackets` dentro dos limites de um par de `brackets` também é um par de `brackets` combinado.

Dado **n** string de `brackets`, determine se cada sequência de `brackets` esta balanceada. Se uma string for balanceada, retorne `YES`. Caso contrário, retorne `NO`.


## 📝 Descrição da Função

Complete a função `isBalanced` dentro do arquivo `balanced_brackets.py`.

`isBalanced` tem o seguinte parâmetro:

* string **`brackets`**: uma string de `brackets`

## ↩️ Retorno

* string: `YES` ou `NO`

## 🔜 Formato da Entrada

A primeira linha contém um único inteiro **n**, o número de strings.

Cada uma das próximas **n** linhas contém uma única string `brackets`, uma sequência de ***Brackets***.

## 🔗 Limitação

* <img src="https://render.githubusercontent.com/render/math?math=1 \le n \le 10^3" style="background: red;">
* <img src="https://render.githubusercontent.com/render/math?math=1 \le |brackets| \le 10^3">, onde <img src="https://render.githubusercontent.com/render/math?math=|brackets|"> é o comprimento da sequência.
* Todos os caracteres ∈ { **`{`**, **`}`**, **`(`**, **`)`**, **`[`**, **`]`** }.

## 🔙 Formato da Saída

Para cada string retorne `YES` ou `NO`

## Exemplo de entrada

Tamanho: `n = 3`

Primeira string: `{[()]}`

Segunda string : `{[(])}`

Terceira string: `{{[[(())]]}}`

## Exemplo de saída

```
YES
NO
YES
```

## 💬 Explicação

1. A string `{[()]}` atende aos dois critérios para ser uma string balanceada.
1. A string `{[(])}` não esta balanceada porque os brackets incluídos pelo par combinado `{` e `}` não são balanceados: `[(])`
1. A string `{{[[(())]]}}` atende aos dois critérios para ser uma string balanceada.

## 🧪 Rodando os testes

Para executar os testes e checar os resultados do desenvolvimento basta rodar o comando abaixo:

```bash
python3 -m unittest
```
