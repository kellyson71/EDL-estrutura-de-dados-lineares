import os

from lista import No


class Polinomio:
    def __init__(self):
        self.cabeca = No(0, 0)

    def inserir(self, coeficiente, grau):
        if coeficiente == 0:
            return

        anterior = self.cabeca
        atual = anterior.proximo

        while atual is not None and atual.grau > grau:
            anterior = atual
            atual = atual.proximo

        if atual is not None and atual.grau == grau:
            atual.coeficiente += coeficiente

            if atual.coeficiente == 0:
                anterior.proximo = atual.proximo

            return

        novo = No(coeficiente, grau)
        novo.proximo = atual
        anterior.proximo = novo

    def grau(self):
        primeiro = self.cabeca.proximo
        return primeiro.grau if primeiro is not None else 0

    def tamanho(self):
        quantidade = 0
        atual = self.cabeca.proximo

        while atual is not None:
            quantidade += 1
            atual = atual.proximo

        return quantidade

    def avaliar(self, x):
        resultado = 0
        atual = self.cabeca.proximo

        while atual is not None:
            resultado += atual.coeficiente * x ** atual.grau
            atual = atual.proximo

        return resultado

    def __add__(self, outro):
        resultado = Polinomio()

        for polinomio in (self, outro):
            atual = polinomio.cabeca.proximo

            while atual is not None:
                resultado.inserir(atual.coeficiente, atual.grau)
                atual = atual.proximo

        return resultado

    def __sub__(self, outro):
        resultado = Polinomio()
        atual = self.cabeca.proximo

        while atual is not None:
            resultado.inserir(atual.coeficiente, atual.grau)
            atual = atual.proximo

        atual = outro.cabeca.proximo

        while atual is not None:
            resultado.inserir(-atual.coeficiente, atual.grau)
            atual = atual.proximo

        return resultado

    def __mul__(self, outro):
        resultado = Polinomio()
        termo1 = self.cabeca.proximo

        while termo1 is not None:
            termo2 = outro.cabeca.proximo

            while termo2 is not None:
                coeficiente = termo1.coeficiente * termo2.coeficiente
                grau = termo1.grau + termo2.grau
                resultado.inserir(coeficiente, grau)
                termo2 = termo2.proximo

            termo1 = termo1.proximo

        return resultado

    def _numero(self, valor):
        return f"{valor:g}"

    def texto(self):
        atual = self.cabeca.proximo

        if atual is None:
            return "0"

        resposta = ""

        while atual is not None:
            coeficiente = atual.coeficiente
            grau = atual.grau
            modulo = abs(coeficiente)

            if resposta == "":
                sinal = "-" if coeficiente < 0 else ""
            else:
                sinal = " - " if coeficiente < 0 else " + "

            if grau == 0:
                termo = self._numero(modulo)
            elif grau == 1:
                numero = "" if modulo == 1 else self._numero(modulo)
                termo = numero + "x"
            else:
                numero = "" if modulo == 1 else self._numero(modulo)
                termo = numero + f"x^{grau}"

            resposta += sinal + termo
            atual = atual.proximo

        return resposta

    def __str__(self):
        return self.texto()


def ler_polinomio(linha):
    numeros = linha.split()

    if len(numeros) % 2 != 0:
        raise ValueError("precisa ter pares")

    polinomio = Polinomio()

    for posicao in range(0, len(numeros), 2):
        coeficiente = float(numeros[posicao])
        grau = int(numeros[posicao + 1])
        polinomio.inserir(coeficiente, grau)

    return polinomio


def tamanho_antes_simplificar(linha):
    numeros = linha.split()

    if len(numeros) % 2 != 0:
        raise ValueError("precisa ter pares")

    quantidade = 0

    for posicao in range(0, len(numeros), 2):
        if float(numeros[posicao]) != 0:
            quantidade += 1

    return quantidade


def executar_arquivo(nome):
    if not os.path.exists(nome):
        print(f"Arquivo '{nome}' nao encontrado.")
        return

    with open(nome, "r", encoding="utf-8") as arquivo:
        linhas = [linha.strip() for linha in arquivo if linha.strip()]

    posicao = 0

    while posicao < len(linhas):
        operacao = linhas[posicao].lower()

        if operacao in ("+", "-", "*"):
            p = ler_polinomio(linhas[posicao + 1])
            q = ler_polinomio(linhas[posicao + 2])

            if operacao == "+":
                resposta = p + q
                nome = "Soma"
            elif operacao == "-":
                resposta = p - q
                nome = "Subtracao"
            else:
                resposta = p * q
                nome = "Multiplicacao"

            print(f"\n{nome}")
            print(f"p(x) = {p}")
            print(f"q(x) = {q}")
            print(f"Resultado = {resposta}")
            posicao += 3

        elif operacao in ("g", "t", "p"):
            linha_polinomio = linhas[posicao + 1]
            p = ler_polinomio(linha_polinomio)

            if operacao == "g":
                print("\nGrau")
                print(f"p(x) = {p}")
                print(f"Grau = {p.grau()}")
            elif operacao == "t":
                print("\nTamanho")
                print(f"p(x) = {p}")
                print(
                    "Antes de simplificar = "
                    f"{tamanho_antes_simplificar(linha_polinomio)}"
                )
                print(f"Depois de simplificar = {p.tamanho()}")
            else:
                print("\nPolinomio")
                print(f"p(x) = {p}")

            posicao += 2

        elif operacao == "a":
            primeira_linha = linhas[posicao + 1]
            segunda_linha = linhas[posicao + 2]

            if len(primeira_linha.split()) == 1:
                x = float(primeira_linha)
                p = ler_polinomio(segunda_linha)
            else:
                p = ler_polinomio(primeira_linha)
                x = float(segunda_linha)

            print("\nAvaliacao")
            print(f"p(x) = {p}")
            print(f"x = {x:g}")
            print(f"Resultado = {p.avaliar(x):g}")
            posicao += 3

        else:
            print(f"Operacao desconhecida: {operacao}")
            posicao += 1


if __name__ == "__main__":
    executar_arquivo("desafio.txt")
