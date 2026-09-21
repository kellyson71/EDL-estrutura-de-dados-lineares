class No:
    def __init__(self, coeficiente, grau):
        self.coeficiente = coeficiente
        self.grau = grau
        self.proximo = None


class Lista:
    def __init__(self):
        self.cabeca = None
        self.quantidade = 0

    def ObterProximo(self, no):
        return no.proximo

    def ObterValor(self, no):
        return no.coeficiente, no.grau

    def Tamanho(self):
        return self.quantidade

    def Existe(self, no):
        atual = self.cabeca

        while atual is not None:
            if atual is no:
                return True
            atual = atual.proximo
            
        return False

    def Buscar(self, coeficiente):
        atual = self.cabeca

        while atual is not None:
            if atual.coeficiente == coeficiente:
                return atual
            atual = atual.proximo

        return None

    def _inserir_no(self, novo):
        if self.cabeca is None or novo.coeficiente < self.cabeca.coeficiente:
            novo.proximo = self.cabeca
            self.cabeca = novo
        else:
            atual = self.cabeca

            while (atual.proximo is not None and
                   atual.proximo.coeficiente <= novo.coeficiente):
                atual = atual.proximo

            novo.proximo = atual.proximo
            atual.proximo = novo

        self.quantidade += 1
        return novo

    def Inserir(self, coeficiente, grau):
        novo = No(coeficiente, grau)
        return self._inserir_no(novo)

    def Destruir(self, no):
        anterior = None
        atual = self.cabeca

        while atual is not None:
            if atual is no:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                atual.proximo = None
                self.quantidade -= 1
                return True

            anterior = atual
            atual = atual.proximo

        return False

    def Excluir(self, coeficiente):
        no = self.Buscar(coeficiente)

        if no is None:
            return False

        return self.Destruir(no)

    def AlterarNo(self, no, novo_coeficiente, novo_grau):
        if not self.Destruir(no):
            return False

        no.coeficiente = novo_coeficiente
        no.grau = novo_grau
        self._inserir_no(no)

        return True

    def mostrarALL(self):
        elementos = []
        atual = self.cabeca

        while atual is not None:
            elementos.append(f"[{atual.coeficiente}, {atual.grau}]")
            atual = atual.proximo

        return " -> ".join(elementos) + " -> None"

    def __del__(self):
        while self.cabeca is not None:
            proximo = self.cabeca.proximo
            self.cabeca.proximo = None
            self.cabeca = proximo

        self.quantidade = 0


if __name__ == "__main__":
    lista = Lista()
    no10 = lista.Inserir(10, 1)
    no5 = lista.Inserir(5, 2)
    lista.Inserir(20, 3)

    print(lista.mostrarALL())
    print(lista.Tamanho())
    print(lista.ObterValor(no5))
    print(lista.ObterValor(lista.ObterProximo(no5)))
    print(lista.Existe(no10))
    print(lista.ObterValor(lista.Buscar(20)))

    lista.AlterarNo(no10, 2, 9)
    print(lista.mostrarALL())

    lista.Excluir(5)
    print(lista.mostrarALL())
