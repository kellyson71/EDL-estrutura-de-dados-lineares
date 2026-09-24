from cell import Cell
from pilha import Pilha


class Maze:
    def __init__(self, linhas):
        self.exitMarker = "e"
        self.entryMarker = "m"
        self.visited = "."
        self.passage = "0"
        self.wall = "1"

        self.mazeStack = Pilha()
        self.maze = self.__inicializarLabirinto(linhas)

        self.entryCell = self.__encontrarMarcador(self.entryMarker)
        self.exitCell = self.__encontrarMarcador(self.exitMarker)
        self.currentCell = self.entryCell

    def __inicializarLabirinto(self, linhas):
        pilhaLinhas = Pilha()
        largura = 0

        for linha in linhas:
            linhaComParedes = self.wall + linha + self.wall
            largura = max(largura, len(linhaComParedes))
            pilhaLinhas.push(linhaComParedes)

        linhaDeParedes = self.wall * largura

        maze = [linhaDeParedes]
        while not pilhaLinhas.vazia():
            maze.append(pilhaLinhas.pop())
        maze.append(linhaDeParedes)

        return maze

    def __encontrarMarcador(self, marcador):
        for x, linha in enumerate(self.maze):
            y = linha.find(marcador)
            if y != -1:
                return Cell(x, y)

        raise ValueError(f"Marcador '{marcador}' nao encontrado no labirinto")

    def __caractere(self, celula):
        return self.maze[celula.getX()][celula.getY()]

    def __marcarVisitado(self, celula):
        linha = self.maze[celula.getX()]
        y = celula.getY()
        self.maze[celula.getX()] = linha[:y] + self.visited + linha[y + 1 :]

    def __vizinhosNaoVisitados(self, celula):
        x, y = celula.getX(), celula.getY()
        # ordem de empilhamento: cima, baixo, esquerda, direita
        candidatos = [Cell(x - 1, y), Cell(x + 1, y), Cell(x, y - 1), Cell(x, y + 1)]

        return [
            candidato
            for candidato in candidatos
            if self.__caractere(candidato) not in (self.wall, self.visited)
        ]

    def exitMaze(self):
        self.mazeStack = Pilha()
        self.currentCell = self.entryCell

        while self.currentCell != self.exitCell:
            self.__marcarVisitado(self.currentCell)

            for vizinho in self.__vizinhosNaoVisitados(self.currentCell):
                self.mazeStack.push(vizinho)

            if self.mazeStack.vazia():
                print("Caminho nao encontrado")
                return

            self.currentCell = self.mazeStack.pop()

        print("Saida encontrada!")

    def __str__(self):
        return "\n".join(self.maze)
