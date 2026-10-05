class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        return None

    def tamanho(self):
        return len(self.itens)

if __name__ == "__main__":
    p = Pilha()
    p.empilhar(1)
    p.empilhar(2)
    p.empilhar(3)
    print("Topo da pilha:", p.topo())
    print("Desempilhou:", p.desempilhar())
    print("Tamanho atual:", p.tamanho())
