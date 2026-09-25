import sys

from maze import Maze

CARACTERES_VALIDOS = {"0", "1", "e", "m"}


def _validarLinha(linha):
    for caractere in linha:
        if caractere not in CARACTERES_VALIDOS:
            raise ValueError(f"Caractere invalido no labirinto: '{caractere}'")


def lerLabirintosDoArquivo(caminho):
    labirintos = []
    linhasAtual = []

    with open(caminho, encoding="utf-8") as arquivo:
        for linhaBruta in arquivo:
            linha = linhaBruta.rstrip("\n").rstrip("\r")

            if linha.strip() == "":
                if linhasAtual:
                    labirintos.append(linhasAtual)
                    linhasAtual = []
                continue

            _validarLinha(linha)
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

        _validarLinha(linha)
        linhas.append(linha)

    return linhas


def resolver(linhas, animado=False):
    labirinto = Maze(linhas)

    if animado:
        labirinto.exitMazeAnimado()
        return

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

    animado = "--animado" in argv
    if animado:
        argv.remove("--animado")

    if argv:
        for linhas in lerLabirintosDoArquivo(argv[0]):
            resolver(linhas, animado)
    else:
        resolver(lerLabirintoDoTeclado(), animado)


if __name__ == "__main__":
    main()
