class Pilha:
    """
    Pilha bem simples, guardando os itens numa lista comum do Python.
    O final da lista e o topo da pilha.
    """

    def __init__(self):
        self.itens = []

    def vazia(self):
        if len(self.itens) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        ultima_posicao = len(self.itens) - 1
        item_do_topo = self.itens[ultima_posicao]
        self.itens.pop(ultima_posicao)
        return item_do_topo
