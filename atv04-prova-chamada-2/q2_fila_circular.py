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


if __name__ == "__main__":
    f = FilaCircular(3)
    print(f.retirar())
    print(f.guardar(10), f.guardar(20), f.guardar(30), f.guardar(40))
    print(f.retirar(), f.retirar())
    print(f.guardar(50), f.guardar(60), f.guardar(70))
    print(f.retirar(), f.retirar(), f.retirar(), f.retirar())
