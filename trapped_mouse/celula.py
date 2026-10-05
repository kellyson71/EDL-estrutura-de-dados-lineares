class Celula:
    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

    def __eq__(self, outra):
        if not isinstance(outra, Celula):
            return False
        return self.linha == outra.linha and self.coluna == outra.coluna
