class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class Pilha:
    def __init__(self):
        self.topo_no = None
        self.tamanho = 0

    def vazia(self):
        return self.topo_no is None

    def push(self, valor):
        novo = No(valor)
        novo.proximo = self.topo_no
        self.topo_no = novo
        self.tamanho += 1

    def pop(self):
        if self.vazia():
            raise IndexError("pop em pilha vazia")

        no = self.topo_no
        self.topo_no = no.proximo
        self.tamanho -= 1
        return no.valor

    def topo(self):
        if self.vazia():
            raise IndexError("topo em pilha vazia")

        return self.topo_no.valor

    def __len__(self):
        return self.tamanho
