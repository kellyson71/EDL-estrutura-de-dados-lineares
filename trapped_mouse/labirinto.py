from celula import Celula
from pilha import Pilha

EMOJIS = {
    "1": "🧱",
    "0": "  ",
    "m": "🐭",
    "e": "🧀",
    ".": "🐾",
}


class Labirinto:
    def __init__(self, linhas):
        self.caractereSaida = "e"
        self.caractereRato = "m"
        self.caractereVisitado = "."
        self.caractereCorredor = "0"
        self.caractereParede = "1"

        self.pilhaParaVisitar = Pilha()
        self.pilhaDoCaminho = Pilha()

        self.mapa = self.montarMapa(linhas)
        self.posicaoInicial = self.procurarPosicao(self.caractereRato)
        self.posicaoSaida = self.procurarPosicao(self.caractereSaida)
        self.posicaoRato = self.posicaoInicial

    def montarMapa(self, linhas):
        pilhaDeLinhas = Pilha()
        for linha in reversed(linhas):
            linhaComParedes = self.caractereParede + linha + self.caractereParede
            pilhaDeLinhas.empilhar(linhaComParedes)

        largura = len(linhas[0]) + 2
        linhaDeParedes = self.caractereParede * largura

        mapa = []
        mapa.append(linhaDeParedes)
        while not pilhaDeLinhas.esta_vazia():
            mapa.append(pilhaDeLinhas.desempilhar())
        mapa.append(linhaDeParedes)
        return mapa

    def procurarPosicao(self, caractere):
        for linha in range(len(self.mapa)):
            for coluna in range(len(self.mapa[linha])):
                if self.mapa[linha][coluna] == caractere:
                    return Celula(linha, coluna)
        raise ValueError("Caractere '" + caractere + "' não encontrado")

    def marcarVisitada(self, celula):
        textoDaLinha = self.mapa[celula.linha]
        antes = textoDaLinha[:celula.coluna]
        depois = textoDaLinha[celula.coluna + 1:]
        self.mapa[celula.linha] = antes + self.caractereVisitado + depois

    def podeVisitar(self, celula):
        caractere = self.mapa[celula.linha][celula.coluna]
        return caractere == self.caractereCorredor or caractere == self.caractereSaida

    def empilharVizinhos(self):
        linha = self.posicaoRato.linha
        coluna = self.posicaoRato.coluna

        cima = Celula(linha - 1, coluna)
        baixo = Celula(linha + 1, coluna)
        esquerda = Celula(linha, coluna - 1)
        direita = Celula(linha, coluna + 1)

        for vizinho in [cima, baixo, esquerda, direita]:
            if self.podeVisitar(vizinho):
                self.pilhaParaVisitar.empilhar(vizinho)

    def estaAoLado(self, celula):
        distanciaLinhas = abs(self.posicaoRato.linha - celula.linha)
        distanciaColunas = abs(self.posicaoRato.coluna - celula.coluna)
        return distanciaLinhas + distanciaColunas == 1

    def moverRatoPara(self, celula, mostrarPasso):
        self.posicaoRato = celula
        if mostrarPasso is not None:
            mostrarPasso()

    def voltarAteFicarAoLado(self, celula, mostrarPasso):
        while not self.estaAoLado(celula):
            celulaAnterior = self.pilhaDoCaminho.desempilhar()
            self.moverRatoPara(celulaAnterior, mostrarPasso)

    def sairDoLabirinto(self, mostrarPasso=None):
        while self.posicaoRato != self.posicaoSaida:
            self.marcarVisitada(self.posicaoRato)
            self.empilharVizinhos()

            if self.pilhaParaVisitar.esta_vazia():
                return False

            proximaCelula = self.pilhaParaVisitar.desempilhar()
            self.voltarAteFicarAoLado(proximaCelula, mostrarPasso)
            self.pilhaDoCaminho.empilhar(self.posicaoRato)
            self.moverRatoPara(proximaCelula, mostrarPasso)

        return True

    def __str__(self):
        texto = ""
        for linha in range(len(self.mapa)):
            for coluna in range(len(self.mapa[linha])):
                if self.posicaoRato == Celula(linha, coluna):
                    texto += EMOJIS[self.caractereRato]
                else:
                    texto += EMOJIS[self.mapa[linha][coluna]]
            texto += "\n"
        return texto
