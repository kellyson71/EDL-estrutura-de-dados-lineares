class FilaCircular:
    def __init__(self, capacidade):
        self.dados = [None] * capacidade
        self.capacidade = capacidade
        self.inicio = 0
        self.tamanho = 0

    def cheia(self):
        return self.tamanho == self.capacidade

    def vazia(self):
        return self.tamanho == 0

    def guardar(self, leitura):
        if self.cheia():
            return False
        fim = (self.inicio + self.tamanho) % self.capacidade
        self.dados[fim] = leitura
        self.tamanho += 1
        return True

    def retirar(self):
        if self.vazia():
            return None
        leitura = self.dados[self.inicio]
        self.dados[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return leitura

