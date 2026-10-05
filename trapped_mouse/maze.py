import os
import time

from cell import Cell
from pilha import Pilha

SIMBOLOS = {
    "1": "🧱",
    "0": "  ",
    "m": "🐭",
    "e": "🧀",
    ".": "🐾",
}


class Maze:
    def __init__(self, linhas):
        self.exitMarker = "e"
        self.entryMarker = "m"
        self.visited = "."
        self.passage = "0"
        self.wall = "1"

        self.mazeStack = Pilha()

        self.maze = self.montarLabirintoComParedes(linhas)

        self.entryCell = self.procurarCelulaDoMarcador(self.entryMarker)
        self.exitCell = self.procurarCelulaDoMarcador(self.exitMarker)
        self.currentCell = self.entryCell

    def montarLabirintoComParedes(self, linhas):
        mazeRows = Pilha()

        for linha in reversed(linhas):
            mazeRows.push(self.wall + linha + self.wall)

        largura = len(linhas[0]) + 2
        parede = self.wall * largura

        maze = [parede]

        while not mazeRows.vazia():
            maze.append(mazeRows.pop())

        maze.append(parede)

        return maze

    def procurarCelulaDoMarcador(self, marcador):
        for linha in range(len(self.maze)):
            for coluna in range(len(self.maze[linha])):
                if self.maze[linha][coluna] == marcador:
                    return Cell(linha, coluna)

        raise ValueError(f"Marcador '{marcador}' não encontrado no labirinto")

    def marcarCelulaComoVisitada(self, celula):
        linha = self.maze[celula.x]
        self.maze[celula.x] = linha[:celula.y] + self.visited + linha[celula.y + 1:]

    def celulaPodeSerVisitada(self, celula):
        caractere = self.maze[celula.x][celula.y]

        if caractere == self.passage:
            return True
        if caractere == self.exitMarker:
            return True
        if caractere == self.entryMarker:
            return True

        return False

    def empilharVizinhosDaCelula(self, celula):
        x, y = celula.x, celula.y
        vizinhos = [
            Cell(x - 1, y),
            Cell(x + 1, y),
            Cell(x, y - 1),
            Cell(x, y + 1),
        ]

        for vizinho in vizinhos:
            if self.celulaPodeSerVisitada(vizinho):
                self.mazeStack.push(vizinho)

    def exitMaze(self, animado=False, delay=0.2):
        self.mazeStack = Pilha()
        self.currentCell = self.entryCell

        if animado:
            self.mostrarLabirintoComRatoNaTela()
            time.sleep(delay)

        while self.currentCell != self.exitCell:
            self.marcarCelulaComoVisitada(self.currentCell)
            self.empilharVizinhosDaCelula(self.currentCell)

            if self.mazeStack.vazia():
                print("Caminho não encontrado!")
                return

            self.currentCell = self.mazeStack.pop()

            if animado:
                self.mostrarLabirintoComRatoNaTela()
                time.sleep(delay)

        print("Saída encontrada!")

    def exitMazeAnimado(self, delay=0.2):
        self.exitMaze(animado=True, delay=delay)

    def formatarLinha(self, linha):
        texto = ""
        for caractere in linha:
            texto += SIMBOLOS.get(caractere, caractere)

        return texto

    def mostrarLabirintoComRatoNaTela(self):
        os.system("cls" if os.name == "nt" else "clear")

        for linhaAtual in range(len(self.maze)):
            linha = self.maze[linhaAtual]

            if linhaAtual == self.currentCell.x:
                y = self.currentCell.y
                linha = linha[:y] + "m" + linha[y + 1:]

            print(self.formatarLinha(linha))

    def __str__(self):
        texto = ""
        for linha in self.maze:
            texto += self.formatarLinha(linha) + "\n"
        return texto
