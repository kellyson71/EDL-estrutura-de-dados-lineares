class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, x):
        self.itens.append(x)

    def desempilhar(self):
        return self.itens.pop()

    def vazia(self):
        return not self.itens


class FilaDePedidos:
    def __init__(self):
        self.entrada = Pilha()
        self.saida = Pilha()
        self.quantidade = 0

    def registrar(self, pedido):
        self.entrada.empilhar(pedido)
        self.quantidade += 1

    def proximo(self):
        if self.saida.vazia():
            while not self.entrada.vazia():
                self.saida.empilhar(self.entrada.desempilhar())
        if self.saida.vazia():
            return None
        self.quantidade -= 1
        return self.saida.desempilhar()

    def aguardando(self):
        return self.quantidade


if __name__ == "__main__":
    f = FilaDePedidos()
    print(f.proximo())
    f.registrar("pedido 1")
    f.registrar("pedido 2")
    print(f.proximo(), f.aguardando())
    f.registrar("pedido 3")
    print(f.proximo(), f.proximo(), f.proximo(), f.aguardando())
