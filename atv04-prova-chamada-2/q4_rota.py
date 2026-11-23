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

