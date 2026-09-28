class Cell:
    """
    Representa uma posicao (x, y) dentro do labirinto.
    Em Python nao existe "privado" de verdade como em Java/C++, entao so
    guardamos x e y como atributos normais mesmo.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, outra_celula):
        # Isso aqui faz o papel do "equals" (Java) / operador "==" (C++)
        # pedido no enunciado: duas celulas sao iguais quando x e y sao iguais.
        if self.x == outra_celula.x and self.y == outra_celula.y:
            return True
        else:
            return False
