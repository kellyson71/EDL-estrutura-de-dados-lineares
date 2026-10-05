import os
import time
from labirinto import Labirinto

SEGUNDOS_POR_PASSO = 0.12


class Terminal:
    def animarLabirintos(self, labirintos):
        total = len(labirintos)

        for indice in range(total):
            self.titulo = "Labirinto " + str(indice + 1) + " de " + str(total)
            linhas = labirintos[indice]
            self.labirinto = Labirinto(linhas)

            self.desenhar()
            input("Aperte ENTER para soltar o rato...")

            achouSaida = self.labirinto.sairDoLabirinto(self.mostrarPasso)

            self.desenhar()
            if achouSaida:
                print("Saída encontrada!")
            else:
                print("Caminho não encontrado!")
            input("Aperte ENTER para continuar...")

    def limparTela(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def desenhar(self):
        self.limparTela()
        print(self.titulo)
        print(self.labirinto)

    def mostrarPasso(self):
        self.desenhar()
        time.sleep(SEGUNDOS_POR_PASSO)
