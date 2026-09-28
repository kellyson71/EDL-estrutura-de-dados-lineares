# Trapped Mouse — anotações

Resumo do que cada arquivo faz e como o algoritmo funciona, pra eu não
esquecer na hora de apresentar.

## O problema

Um rato (`m`) precisa sair de um labirinto até a saída (`e`), andando por
corredores (`0`) e sem atravessar paredes (`1`). Ele vai testando os
caminhos sistematicamente e, quando entra num beco sem saída, volta pelo
caminho até achar um lugar com outra opção não testada ainda
(backtracking).

## Arquivos

| Arquivo         | O que tem                                                            |
| --------------- | --------------------------------------------------------------------- |
| `pilha.py`      | Classe `Pilha` (push, pop, vazia). Estrutura pedida pela atividade.   |
| `cell.py`       | Classe `Cell` — só guarda `x` e `y` de uma posição do labirinto.      |
| `maze.py`       | Classe `Maze` — monta o labirinto e resolve com `exitMaze()`.         |
| `main.py`       | Programa que lê o labirinto (arquivo ou teclado) e chama `Maze`.      |
| `entrada1.txt`  | Labirinto pequeno, é o mesmo exemplo que tem no slide da atividade.   |
| `entrada2.txt`  | Outro labirinto pequeno, pra testar.                                  |
| `entrada3.txt`  | Labirinto grande, 20x20, gerado só pra mostrar que funciona em maior. |

## Os dois algoritmos (do jeito que o slide pede)

**1. Montar o labirinto** (`montarLabirintoComParedes` em `maze.py`)

Empilha cada linha digitada (já com parede nas duas pontas), depois
desempilha tudo botando uma linha de parede em cima e outra embaixo.
Como é uma pilha, isso *inverte* a ordem das linhas — é assim mesmo que o
slide descreve, não é bug.

**2. Sair do labirinto** (`exitMaze` em `maze.py`)

```
enquanto o rato não estiver na saída:
    marca a posição atual como visitada (.)
    empilha os vizinhos (cima, baixo, esquerda, direita) que ainda não
    foram visitados e não são parede
    se a pilha estiver vazia -> não tem caminho, acabou
    senão -> tira uma célula do topo da pilha e vai pra ela
```

A ordem de **testar** os vizinhos que o slide pede é: direita, esquerda,
baixo, cima. Só que numa pilha quem sai primeiro é quem entrou por
último — então pra "direita" ser testado primeiro, ele precisa ser
empilhado por último. Por isso no código a ordem de empilhar é o
contrário: cima, baixo, esquerda, direita.

## Legenda dos caracteres

| Caractere | Significado                    |
| --------- | ------------------------------- |
| `1`       | parede                          |
| `0`       | corredor (ainda não andado)     |
| `m`       | posição inicial do rato         |
| `e`       | saída do labirinto              |
| `.`       | corredor já visitado pelo rato  |

## Exemplo pequeno (`entrada1.txt`, o do slide)

Antes de rodar `exitMaze()`:

```
111111
100m11
1000e1
111001
111111
```

Depois de rodar (`.` é o caminho que o rato percorreu):

```
111111
1...11
1...e1
111001
111111
```

## Labirinto grande (`entrada3.txt`, 20x20)

Antes:

```
1111111111111111111111
1111111111111111111111
1000100000000000000e11
1110101111111110111111
1000101000001010000011
1011101110101011111011
1010001000100010000011
1010111011111010111011
1000100010001010100011
1011111010111010101111
1000000010000010101011
1111111011111110101011
1000100010000000100011
1011101110111111111011
1000000010100010000011
1011111110101010111111
1010001000101010100011
1010101011101010101111
1010100010001000100011
1110111110111111111011
1m00100000000000000011
1111111111111111111111
```

Depois de resolver:

```
1111111111111111111111
1111111111111111111111
100010000000000....e11
111010111111111.111111
100010100000101.....11
1011101110101011111.11
101000100010001.....11
101011101111101.111.11
100010001000101.1...11
101111101011101.1.1111
100000001000001.1.1.11
111111101111111.1.1.11
100010001.......1...11
101110111.111111111.11
100000001.1...1.....11
101111111.1.1.1.111111
101...1...1.1.1.1...11
101.1.1.111.1.1.1.1111
101.1...1...1...1...11
111.11111.111111111.11
1...1...............11
1111111111111111111111
```

Dá pra ver o caminho de `.` saindo do `m` (canto inferior esquerdo) até o
`e` (canto superior direito).

## Como rodar

```bash
python3 main.py entrada1.txt            # mostra labirinto antes/depois
python3 main.py entrada1.txt --animado  # anima o rato andando no terminal
python3 main.py                         # digita o labirinto na mão
```
