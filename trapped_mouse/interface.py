import os
import sys
import pygame
from labirinto import Labirinto

CAMINHO_DESTE_ARQUIVO = os.path.abspath(__file__)
PASTA = os.path.dirname(CAMINHO_DESTE_ARQUIVO)
CAMINHO_FOTO_RATO = os.path.join(PASTA, "assets", "mouse_transparent.png")

LARGURA_JANELA = 720
ALTURA_JANELA = 800
ALTURA_DA_BARRA = 80
TAMANHO_MAXIMO_CELULA = 90
PASSOS_POR_SEGUNDO = 8

COR_FUNDO = (24, 32, 42)
COR_TEXTO = (240, 243, 246)
CORES_DAS_CELULAS = {
    "1": (52, 73, 94),
    "0": (245, 246, 250),
    "m": (245, 246, 250),
    ".": (174, 214, 241),
    "e": (241, 196, 15),
}


class Interface:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Trapped Mouse")

        self.tela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
        self.fonte = pygame.font.SysFont("Arial", 22)
        self.relogio = pygame.time.Clock()

        fotoCarregada = pygame.image.load(CAMINHO_FOTO_RATO)
        self.fotoRatoOriginal = fotoCarregada.convert_alpha()

    def animarLabirintos(self, labirintos):
        total = len(labirintos)

        for indice in range(total):
            self.titulo = "Labirinto " + str(indice + 1) + " de " + str(total)
            linhas = labirintos[indice]
            self.labirinto = Labirinto(linhas)
            self.calcularTamanhos()

            self.mensagem = "Aperte ESPAÇO para soltar o rato"
            self.esperarEspaco()

            self.mensagem = "Procurando a saída..."
            achouSaida = self.labirinto.sairDoLabirinto(self.mostrarPasso)

            if achouSaida:
                self.mensagem = "Saída encontrada! Aperte ESPAÇO para continuar"
            else:
                self.mensagem = "Caminho não encontrado! Aperte ESPAÇO para continuar"
            self.esperarEspaco()

        pygame.quit()

    def calcularTamanhos(self):
        quantidadeLinhas = len(self.labirinto.mapa)
        quantidadeColunas = len(self.labirinto.mapa[0])

        tamanhoPelaLargura = LARGURA_JANELA // quantidadeColunas
        tamanhoPelaAltura = (ALTURA_JANELA - ALTURA_DA_BARRA) // quantidadeLinhas
        self.tamanhoCelula = min(tamanhoPelaLargura, tamanhoPelaAltura, TAMANHO_MAXIMO_CELULA)

        larguraLabirinto = quantidadeColunas * self.tamanhoCelula
        alturaLabirinto = quantidadeLinhas * self.tamanhoCelula
        self.margemEsquerda = (LARGURA_JANELA - larguraLabirinto) // 2
        self.margemTopo = ALTURA_DA_BARRA + (ALTURA_JANELA - ALTURA_DA_BARRA - alturaLabirinto) // 2

        alturaRato = self.tamanhoCelula
        larguraRato = alturaRato * self.fotoRatoOriginal.get_width() // self.fotoRatoOriginal.get_height()
        self.fotoRatoRedimensionada = pygame.transform.smoothscale(self.fotoRatoOriginal, (larguraRato, alturaRato))

    def fecharSeUsuarioPediu(self, evento):
        clicouNoX = evento.type == pygame.QUIT
        apertouEsc = evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE

        if clicouNoX or apertouEsc:
            pygame.quit()
            sys.exit()

    def esperarEspaco(self):
        while True:
            for evento in pygame.event.get():
                self.fecharSeUsuarioPediu(evento)
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                    return

            self.desenhar()
            self.relogio.tick(PASSOS_POR_SEGUNDO)

    def mostrarPasso(self):
        for evento in pygame.event.get():
            self.fecharSeUsuarioPediu(evento)

        self.desenhar()
        self.relogio.tick(PASSOS_POR_SEGUNDO)

    def escrever(self, texto, x, y):
        imagemTexto = self.fonte.render(texto, True, COR_TEXTO)
        self.tela.blit(imagemTexto, (x, y))

    def quadradoDaCelula(self, linha, coluna):
        esquerda = self.margemEsquerda + coluna * self.tamanhoCelula
        topo = self.margemTopo + linha * self.tamanhoCelula
        lado = self.tamanhoCelula - 1
        return pygame.Rect(esquerda, topo, lado, lado)

    def desenharLabirinto(self):
        mapa = self.labirinto.mapa

        for linha in range(len(mapa)):
            for coluna in range(len(mapa[linha])):
                caractere = mapa[linha][coluna]
                cor = CORES_DAS_CELULAS[caractere]
                quadrado = self.quadradoDaCelula(linha, coluna)
                pygame.draw.rect(self.tela, cor, quadrado)

    def desenharRato(self):
        celula = self.labirinto.posicaoRato
        quadrado = self.quadradoDaCelula(celula.linha, celula.coluna)

        retanguloRato = self.fotoRatoRedimensionada.get_rect()
        retanguloRato.center = quadrado.center
        self.tela.blit(self.fotoRatoRedimensionada, retanguloRato)

    def desenhar(self):
        self.tela.fill(COR_FUNDO)
        self.escrever(self.titulo, 12, 10)
        self.escrever(self.mensagem, 12, 42)
        self.desenharLabirinto()
        self.desenharRato()
        pygame.display.flip()
