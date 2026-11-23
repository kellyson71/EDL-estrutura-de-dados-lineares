class No:
    def __init__(self, cliente):
        self.cliente = cliente
        self.anterior = None
        self.proximo = None


class FilaSuporte:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def chegada_vip(self, cliente):
        no = No(cliente)
        if self.inicio is None:
            self.inicio = no
            self.fim = no
        else:
            no.proximo = self.inicio
            self.inicio.anterior = no
            self.inicio = no
        self.tamanho += 1

    def chegada_comum(self, cliente):
        no = No(cliente)
        if self.fim is None:
            self.inicio = no
            self.fim = no
        else:
            no.anterior = self.fim
            self.fim.proximo = no
            self.fim = no
        self.tamanho += 1

    def atender(self):
        if self.inicio is None:
            return None
        no = self.inicio
        self.inicio = no.proximo
        if self.inicio is None:
            self.fim = None
        else:
            self.inicio.anterior = None
        self.tamanho -= 1
        return no.cliente

    def desistencia(self):
        if self.fim is None:
            return None
        no = self.fim
        self.fim = no.anterior
        if self.fim is None:
            self.inicio = None
        else:
            self.fim.proximo = None
        self.tamanho -= 1
        return no.cliente

    def esperando(self):
        return self.tamanho

