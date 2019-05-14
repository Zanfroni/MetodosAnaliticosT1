# MetodosAnaliticosT1
Primeiro trabalho da disciplina de Simulação e Métodos Analíticos do curso de Engenharia de Software, PUCRS

Integrantes: Annderson Packeiser Oreto, Ezequiel Rinco e Gabriel Franzoni

COMO EXECUTAR O ALGORITMO:
==========================

Requisitos: Python3 (versao 3.5 ou superior recomendada)

Para executar este algoritmo, basta ter o arquivo de texto de entrada
(no caso como padrao, chanin.txt) no mesmo diretorio que o main.py
esta localizado.

Deve-se entao digitar o comando python3 main.py

VARIAVEIS QUE PODEM SER MANIPULADAS
===================================

A seguir, estao algumas variaveis no codigo que podem ser
manipuladas para diferentes resultados (e suas localizacoes):

ARQUIVO DE ENTRADA --> .txt (reader(), linha 18)
ACTUAL TIME --> tempo arbitrario inicial (main(), linha 20)
ITERATIONS --> iteracoes da simulacao (main(), linha 21)
GERADOR --> entradas para o gerador (generator(), linhas 15-19)

COMO FUNCIONA O ARQUIVO DE ENTRADA
==================================

A leitura sera feita da seguinte forma:

- Ele le o Size X, onde X representa quantas filas estarao no sistema.
Nota-se que o tamanho de filas do sistema e as filas declaradas no .txt
deve ser igual.

- Ele finalmente lê fila por fila. Onde cada coisa representa o seguinte:
--- QX: id da fila
--- Next: probabilidade de rotacionar para outra fila proxima
--- Same: probabilidade de rotacionar para ela mesma
--- Out: probabilidade de rotacionar para fora do sistema
--- C: servidor
--- K: capacidade
--- CH: tempos de entrada
--- SA: tempos de saida
OBS: As probabilidades precisam totalizar 1

OBSERVACOES:
============

Existem dois diretorios a mais, onde um possui outras entradas
.txt para serem testadas recomendadas para ver as diferencas
na execucao da simulacao. O outro diretorio contem um grafico gerado
a partir das variaveis padrao que inserimos no gerador com objetivo de
mostrar a aleatoriedade dos numeros pseudo-aleatorios
dos exemplos. Lembre-se de copiar os conteudos dos exemplos de entrada
para chanin.txt.

O objetivo deste trabalho nosso foi entender o conceito de simulacao
de situacoes por numeros pseudo-aleatorios, com probabilidades de
rotacao.
