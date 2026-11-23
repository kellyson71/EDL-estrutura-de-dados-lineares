class No:
    def __init__(self, jogador):
        self.jogador = jogador
        self.proximo = None


class Roda:
    def __init__(self):
        self.anterior = None
        self.tamanho = 0

    def entrar(self, jogador):
        no = No(jogador)
        if self.anterior is None:
            no.proximo = no
            self.anterior = no
        else:
            no.proximo = self.anterior.proximo
            self.anterior.proximo = no
            self.anterior = no
        self.tamanho += 1

    def da_vez(self):
        if self.anterior is None:
            return None
        return self.anterior.proximo.jogador

    def avancar(self, k):
        if self.tamanho == 0:
            return
        for _ in range(k % self.tamanho):
            self.anterior = self.anterior.proximo

    def eliminar(self):
        if self.anterior is None:
            return None
        atual = self.anterior.proximo
        if atual is self.anterior:
            self.anterior = None
        else:
            self.anterior.proximo = atual.proximo
        self.tamanho -= 1
        return atual.jogador

    def simular(self, k):
        if self.tamanho == 0:
            return None
        while self.tamanho > 1:
            self.avancar(k)
            self.eliminar()
        return self.da_vez()

