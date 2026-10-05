import os

from maze import Maze

CARACTERES_VALIDOS = ["0", "1", "e", "m"]


def linhaEhValida(linha):
    for caractere in linha:
        if caractere not in CARACTERES_VALIDOS:
            return False
    return True


def lerLabirintosDoArquivo(caminho):
    with open(caminho, encoding="utf-8") as arquivo:
        linhas = [linha.strip() for linha in arquivo]

    labirintos = []
    labirintoAtual = []

    for linha in linhas:
        if linha == "":
            if labirintoAtual:
                labirintos.append(labirintoAtual)
                labirintoAtual = []
        else:
            if not linhaEhValida(linha):
                raise ValueError("Caractere inválido na linha: " + linha)
            labirintoAtual.append(linha)

    if labirintoAtual:
        labirintos.append(labirintoAtual)

    return labirintos


def lerLabirintoDoTeclado():
    print("Digite as linhas do labirinto (linha vazia pra terminar):")
    linhas = []

    while True:
        linha = input().strip()

        if linha == "":
            break

        if not linhaEhValida(linha):
            print("Caractere inválido, só pode usar: 0, 1, e, m")
            continue

        linhas.append(linha)

    return linhas


def main():
    print("Escolha uma opção:")
    print("1 - Ler labirinto de arquivo")
    print("2 - Digitar labirinto no teclado")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        caminho = input("Digite o nome ou caminho do arquivo: ").strip()

        if not os.path.exists(caminho):
            pasta = os.path.dirname(os.path.abspath(__file__))
            caminho = os.path.join(pasta, caminho)

        for labirinto in lerLabirintosDoArquivo(caminho):
            maze = Maze(labirinto)
            maze.exitMazeAnimado()

    elif opcao == "2":
        linhas = lerLabirintoDoTeclado()
        if linhas:
            maze = Maze(linhas)
            maze.exitMazeAnimado()
        else:
            print("Nenhuma linha digitada.")
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()
