import sys

from maze import Maze


def lerLabirintosDoArquivo(caminho):
    labirintos = []
    linhasAtual = []

    with open(caminho, encoding="utf-8") as arquivo:
        for linhaBruta in arquivo:
            linha = linhaBruta.rstrip("\n")

            if linha.strip() == "":
                if linhasAtual:
                    labirintos.append(linhasAtual)
                    linhasAtual = []
                continue

            linhasAtual.append(linha)

    if linhasAtual:
        labirintos.append(linhasAtual)

    return labirintos


def lerLabirintoDoTeclado():
    print("Digite as linhas do labirinto (linha vazia para terminar):")
    linhas = []

    while True:
        linha = input()
        if linha == "":
            break

        linhas.append(linha)

    return linhas


def resolver(linhas):
    labirinto = Maze(linhas)

    print("Labirinto inicial:")
    print(labirinto)
    print()

    labirinto.exitMaze()
    print()

    print("Labirinto final:")
    print(labirinto)
    print()


def main():
    argv = sys.argv[1:]

    if argv:
        for linhas in lerLabirintosDoArquivo(argv[0]):
            resolver(linhas)
    else:
        resolver(lerLabirintoDoTeclado())


if __name__ == "__main__":
    main()
