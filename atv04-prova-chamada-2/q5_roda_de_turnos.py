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
        da_vez = self.anterior.proximo
        if da_vez is self.anterior:
            self.anterior = None
        else:
            self.anterior.proximo = da_vez.proximo
        self.tamanho -= 1
        return da_vez.jogador

    def simular(self, k):
        if self.tamanho == 0:
            return None
        while self.tamanho > 1:
            self.avancar(k)
            self.eliminar()
        return self.da_vez()


if __name__ == "__main__":
    r = Roda()
    print(r.da_vez(), r.eliminar(), r.simular(3))
    for j in ["Ana", "Bia", "Caio", "Davi", "Eva"]:
        r.entrar(j)
    print(r.da_vez())
    r.avancar(1000000007)
    print(r.da_vez())
    print(r.eliminar(), r.da_vez())
    r2 = Roda()
    for j in range(1, 8):
        r2.entrar(j)
    print(r2.simular(3))
    r3 = Roda()
    r3.entrar("Unico")
    print(r3.simular(5), r3.eliminar(), r3.da_vez())
