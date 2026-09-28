import os
import time

from cell import Cell
from pilha import Pilha


class Maze:
    def __init__(self, linhas_digitadas_pelo_usuario):
        self.exitMarker = "e"
        self.entryMarker = "m"
        self.visited = "."
        self.passage = "0"
        self.wall = "1"

        self.mazeStack = Pilha()

        self.maze = self.montarLabirintoComParedes(linhas_digitadas_pelo_usuario)

        self.entryCell = self.procurarCelulaDoMarcador(self.entryMarker)
        self.exitCell = self.procurarCelulaDoMarcador(self.exitMarker)
        self.currentCell = self.entryCell

    def montarLabirintoComParedes(self, linhas_digitadas_pelo_usuario):
        """
        Algoritmo 1 do slide: coloca uma parede na ponta esquerda e na ponta
        direita de cada linha, empilha todas as linhas e depois desempilha
        tudo, colocando uma linha de parede no topo e outra embaixo.
        """
        pilha_de_linhas = Pilha()

        for linha in linhas_digitadas_pelo_usuario:
            linha_com_paredes_nas_pontas = self.wall + linha + self.wall
            pilha_de_linhas.push(linha_com_paredes_nas_pontas)

        largura_do_labirinto = len(linha_com_paredes_nas_pontas)
        linha_so_de_parede = ""
        for _ in range(largura_do_labirinto):
            linha_so_de_parede = linha_so_de_parede + self.wall

        maze_montado = []
        maze_montado.append(linha_so_de_parede)

        while pilha_de_linhas.vazia() == False:
            linha_desempilhada = pilha_de_linhas.pop()
            maze_montado.append(linha_desempilhada)

        maze_montado.append(linha_so_de_parede)

        return maze_montado

    def procurarCelulaDoMarcador(self, marcador_procurado):
        numero_da_linha = 0
        while numero_da_linha < len(self.maze):
            linha = self.maze[numero_da_linha]

            numero_da_coluna = 0
            while numero_da_coluna < len(linha):
                caractere = linha[numero_da_coluna]
                if caractere == marcador_procurado:
                    return Cell(numero_da_linha, numero_da_coluna)
                numero_da_coluna = numero_da_coluna + 1

            numero_da_linha = numero_da_linha + 1

        raise ValueError("Nao encontrei o marcador '" + marcador_procurado + "' no labirinto")

    def caractereNaCelula(self, celula):
        linha = self.maze[celula.x]
        return linha[celula.y]

    def marcarCelulaComoVisitada(self, celula):
        linha_antiga = self.maze[celula.x]

        linha_nova = ""
        coluna = 0
        while coluna < len(linha_antiga):
            if coluna == celula.y:
                linha_nova = linha_nova + self.visited
            else:
                linha_nova = linha_nova + linha_antiga[coluna]
            coluna = coluna + 1

        self.maze[celula.x] = linha_nova

    def celulaPodeSerVisitada(self, celula):
        caractere = self.caractereNaCelula(celula)

        if caractere == self.wall:
            return False
        if caractere == self.visited:
            return False

        return True

    def empilharVizinhosDaCelula(self, celula):
        """
        A ordem que o enunciado pede pra TESTAR os caminhos e:
        direita, esquerda, baixo, cima.

        Como e uma pilha (o ultimo que entra e o primeiro que sai), pra
        "direita" ser testado primeiro ele precisa ser o ULTIMO a ser
        empilhado. Por isso aqui embaixo a ordem de empilhar e o contrario:
        cima, baixo, esquerda, direita.
        """
        celula_de_cima = Cell(celula.x - 1, celula.y)
        celula_de_baixo = Cell(celula.x + 1, celula.y)
        celula_da_esquerda = Cell(celula.x, celula.y - 1)
        celula_da_direita = Cell(celula.x, celula.y + 1)

        if self.celulaPodeSerVisitada(celula_de_cima):
            self.mazeStack.push(celula_de_cima)

        if self.celulaPodeSerVisitada(celula_de_baixo):
            self.mazeStack.push(celula_de_baixo)

        if self.celulaPodeSerVisitada(celula_da_esquerda):
            self.mazeStack.push(celula_da_esquerda)

        if self.celulaPodeSerVisitada(celula_da_direita):
            self.mazeStack.push(celula_da_direita)

    def exitMaze(self):
        """
        Algoritmo 2 do slide: o rato marca a celula atual como visitada,
        empilha os vizinhos que ainda nao foram visitados e, se a pilha
        nao estiver vazia, tira uma celula do topo e continua por ela.
        Se a pilha ficar vazia antes de chegar na saida, nao tem caminho.
        """
        self.mazeStack = Pilha()
        self.currentCell = self.entryCell

        while self.currentCell != self.exitCell:
            self.marcarCelulaComoVisitada(self.currentCell)
            self.empilharVizinhosDaCelula(self.currentCell)

            if self.mazeStack.vazia() == True:
                print("Caminho nao encontrado")
                return

            self.currentCell = self.mazeStack.pop()

        print("Saida encontrada!")

    def exitMazeAnimado(self, segundos_entre_passos=0.2):
        """
        Faz a mesma coisa que exitMaze, mas vai limpando a tela e
        mostrando o labirinto passo a passo, com o rato ('m') na posicao
        atual. E o ponto extra da animacao pelo terminal.
        """
        self.mazeStack = Pilha()
        self.currentCell = self.entryCell

        self.mostrarLabirintoComRatoNaTela()
        time.sleep(segundos_entre_passos)

        while self.currentCell != self.exitCell:
            self.marcarCelulaComoVisitada(self.currentCell)
            self.empilharVizinhosDaCelula(self.currentCell)

            if self.mazeStack.vazia() == True:
                print("Caminho nao encontrado")
                return

            self.currentCell = self.mazeStack.pop()

            self.mostrarLabirintoComRatoNaTela()
            time.sleep(segundos_entre_passos)

        print("Saida encontrada!")

    def mostrarLabirintoComRatoNaTela(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

        linha_do_rato = self.maze[self.currentCell.x]
        coluna_do_rato = self.currentCell.y

        linha_com_rato_desenhado = ""
        coluna = 0
        while coluna < len(linha_do_rato):
            if coluna == coluna_do_rato:
                linha_com_rato_desenhado = linha_com_rato_desenhado + "m"
            else:
                linha_com_rato_desenhado = linha_com_rato_desenhado + linha_do_rato[coluna]
            coluna = coluna + 1

        numero_da_linha = 0
        while numero_da_linha < len(self.maze):
            if numero_da_linha == self.currentCell.x:
                print(linha_com_rato_desenhado)
            else:
                print(self.maze[numero_da_linha])
            numero_da_linha = numero_da_linha + 1

    def __str__(self):
        texto_do_labirinto = ""

        for linha in self.maze:
            texto_do_labirinto = texto_do_labirinto + linha + "\n"

        return texto_do_labirinto
