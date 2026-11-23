class Parada:
    def __init__(self, endereco):
        self.endereco = endereco
        self.proxima = None


def tem_ciclo(inicio):
    lenta = inicio
    rapida = inicio
    while rapida is not None and rapida.proxima is not None:
        lenta = lenta.proxima
        rapida = rapida.proxima.proxima
        if lenta is rapida:
            return True
    return False


def remover_k_do_fim(inicio, k):
    if k < 1:
        return inicio
    rapido = inicio
    for _ in range(k):
        if rapido is None:
            return inicio
        rapido = rapido.proxima
    if rapido is None:
        return inicio.proxima
    lento = inicio
    while rapido.proxima is not None:
        rapido = rapido.proxima
        lento = lento.proxima
    lento.proxima = lento.proxima.proxima
    return inicio


def criar(enderecos):
    inicio = None
    ultimo = None
    for e in enderecos:
        no = Parada(e)
        if inicio is None:
            inicio = no
        else:
            ultimo.proxima = no
        ultimo = no
    return inicio


def mostrar(inicio):
    r = []
    while inicio is not None:
        r.append(inicio.endereco)
        inicio = inicio.proxima
    return r


if __name__ == "__main__":
    print(tem_ciclo(None))
    a = criar(["A"])
    print(tem_ciclo(a))
    a.proxima = a
    print(tem_ciclo(a))
    r = criar(["A", "B", "C", "D"])
    c = r.proxima.proxima
    c.proxima.proxima = r.proxima
    print(tem_ciclo(r))
    print(mostrar(remover_k_do_fim(criar(["A", "B", "C", "D"]), 1)))
    print(mostrar(remover_k_do_fim(criar(["A", "B", "C", "D"]), 2)))
    print(mostrar(remover_k_do_fim(criar(["A", "B", "C", "D"]), 4)))
    print(mostrar(remover_k_do_fim(criar(["A", "B", "C", "D"]), 5)))
    print(mostrar(remover_k_do_fim(criar(["A"]), 1)))
    print(mostrar(remover_k_do_fim(None, 1)))
