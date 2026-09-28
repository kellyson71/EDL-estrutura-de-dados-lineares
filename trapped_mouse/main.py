import sys

from maze import Maze

CARACTERES_VALIDOS = ["0", "1", "e", "m"]


def linhaEhValida(linha):
    for caractere in linha:
        if caractere not in CARACTERES_VALIDOS:
            return False
    return True


def lerLabirintosDoArquivo(caminho_do_arquivo):
    arquivo = open(caminho_do_arquivo, encoding="utf-8")

    todos_os_labirintos = []
    linhas_do_labirinto_atual = []

    for linha_bruta in arquivo:
        linha = linha_bruta.rstrip("\n")
        linha = linha.rstrip("\r")

        if linha.strip() == "":
            if len(linhas_do_labirinto_atual) > 0:
                todos_os_labirintos.append(linhas_do_labirinto_atual)
                linhas_do_labirinto_atual = []
            continue

        if linhaEhValida(linha) == False:
            raise ValueError("Caractere invalido na linha: " + linha)

        linhas_do_labirinto_atual.append(linha)

    arquivo.close()

    if len(linhas_do_labirinto_atual) > 0:
        todos_os_labirintos.append(linhas_do_labirinto_atual)

    return todos_os_labirintos


def lerLabirintoDoTeclado():
    print("Digite as linhas do labirinto (linha vazia pra terminar):")

    linhas_digitadas = []
    while True:
        linha = input()
        if linha == "":
            break

        if linhaEhValida(linha) == False:
            print("Caractere invalido, so pode usar: 0, 1, e, m")
            continue

        linhas_digitadas.append(linha)

    return linhas_digitadas


def resolverLabirinto(linhas, animado):
    labirinto = Maze(linhas)

    if animado == True:
        labirinto.exitMazeAnimado()
        return

    print("Labirinto inicial:")
    print(labirinto)

    labirinto.exitMaze()
    print()

    print("Labirinto final:")
    print(labirinto)


def main():
    argumentos = sys.argv[1:]

    animado = False
    if "--animado" in argumentos:
        animado = True
        argumentos.remove("--animado")

    if len(argumentos) > 0:
        caminho_do_arquivo = argumentos[0]
        labirintos_do_arquivo = lerLabirintosDoArquivo(caminho_do_arquivo)

        for linhas_de_um_labirinto in labirintos_do_arquivo:
            resolverLabirinto(linhas_de_um_labirinto, animado)
    else:
        linhas_digitadas = lerLabirintoDoTeclado()
        resolverLabirinto(linhas_digitadas, animado)


if __name__ == "__main__":
    main()
