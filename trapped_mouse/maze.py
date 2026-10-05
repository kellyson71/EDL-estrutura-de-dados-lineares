from cell import Cell
from pilha import Pilha

SIMBOLOS = {"1": "🧱", "0": "  ", "m": "🐭", "e": "🧀", ".": "🐾"}


class Maze:
    def __init__(self, linhas):
        self.exitMarker = "e"
        self.entryMarker = "m"
        self.visited = "."
        self.passage = "0"
        self.wall = "1"

        self.mazeStack = Pilha()
        self.maze = self.montarLabirinto(linhas)

        self.entryCell = self.procurarCelula(self.entryMarker)
        self.exitCell = self.procurarCelula(self.exitMarker)
        self.currentCell = self.entryCell

    def montarLabirinto(self, linhas):
        mazeRows = Pilha()
        for linha in reversed(linhas):
            mazeRows.push(self.wall + linha + self.wall)

        parede = self.wall * (len(linhas[0]) + 2)
        maze = [parede]
        while not mazeRows.vazia():
            maze.append(mazeRows.pop())
        maze.append(parede)
        return maze

    def procurarCelula(self, marcador):
        for x in range(len(self.maze)):
            y = self.maze[x].find(marcador)
            if y != -1:
                return Cell(x, y)
        raise ValueError("Marcador '" + marcador + "' não encontrado")

    def marcarVisitada(self, celula):
        linha = self.maze[celula.x]
        self.maze[celula.x] = linha[:celula.y] + self.visited + linha[celula.y + 1:]

    def podeVisitar(self, celula):
        caractere = self.maze[celula.x][celula.y]
        return caractere == self.passage or caractere == self.exitMarker

    def empilharVizinhos(self, celula):
        x = celula.x
        y = celula.y
        vizinhos = [Cell(x - 1, y), Cell(x + 1, y), Cell(x, y - 1), Cell(x, y + 1)]
        for vizinho in vizinhos:
            if self.podeVisitar(vizinho):
                self.mazeStack.push(vizinho)

    def exitMaze(self, aoMover=None):
        self.mazeStack = Pilha()
        self.currentCell = self.entryCell

        while self.currentCell != self.exitCell:
            self.marcarVisitada(self.currentCell)
            self.empilharVizinhos(self.currentCell)

            if self.mazeStack.vazia():
                return False

            self.currentCell = self.mazeStack.pop()
            if aoMover is not None:
                aoMover()

        return True

    def __str__(self):
        texto = ""
        for x in range(len(self.maze)):
            for y in range(len(self.maze[x])):
                if x == self.currentCell.x and y == self.currentCell.y:
                    texto += SIMBOLOS["m"]
                else:
                    texto += SIMBOLOS[self.maze[x][y]]
            texto += "\n"
        return texto
