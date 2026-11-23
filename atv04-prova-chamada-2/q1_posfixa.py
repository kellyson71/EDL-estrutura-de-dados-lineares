class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, x):
        self.itens.append(x)

    def desempilhar(self):
        return self.itens.pop()

    def tamanho(self):
        return len(self.itens)


def avaliar(simbolos):
    pilha = Pilha()
    for s in simbolos:
        if s in ("+", "-", "*", "/"):
            if pilha.tamanho() < 2:
                return "Erro: operador sem operandos suficientes."
            b = pilha.desempilhar()
            a = pilha.desempilhar()
            if s == "+":
                pilha.empilhar(a + b)
            elif s == "-":
                pilha.empilhar(a - b)
            elif s == "*":
                pilha.empilhar(a * b)
            else:
                if b == 0:
                    return "Erro: divisão por zero."
                pilha.empilhar(a / b)
        else:
            pilha.empilhar(float(s))
    if pilha.tamanho() != 1:
        return "Erro: expressão sem resultado único."
    return pilha.desempilhar()

