from leitura import lerLabirintosDoArquivo, lerLabirintoDoTeclado
from terminal import Terminal
from interface import Interface

ARQUIVO_PADRAO = "entrada_multipla.txt"


def escolherEntrada():
    print()
    print("De onde vem o labirinto?")
    print("  1 - Arquivo")
    print("  2 - Teclado")
    print("  0 - Sair")
    return input("Opção: ").strip()


def carregarLabirintos(opcao):
    if opcao == "1":
        nomeArquivo = input("Nome do arquivo (ENTER = " + ARQUIVO_PADRAO + "): ").strip()
        if nomeArquivo == "":
            nomeArquivo = ARQUIVO_PADRAO
        return lerLabirintosDoArquivo(nomeArquivo)

    if opcao == "2":
        labirinto = lerLabirintoDoTeclado()
        return [labirinto]

    raise ValueError("Opção inválida.")


def escolherAnimacao():
    print()
    print("Onde mostrar a animação?")
    print("  1 - Terminal")
    print("  2 - Interface gráfica")
    return input("Opção: ").strip()


def mostrarAnimacao(labirintos):
    opcao = escolherAnimacao()
    while opcao != "1" and opcao != "2":
        print("Opção inválida.")
        opcao = escolherAnimacao()

    if opcao == "1":
        terminal = Terminal()
        terminal.animarLabirintos(labirintos)
    else:
        interface = Interface()
        interface.animarLabirintos(labirintos)


def main():
    opcao = escolherEntrada()

    while opcao != "0":
        try:
            labirintos = carregarLabirintos(opcao)
            mostrarAnimacao(labirintos)
        except FileNotFoundError:
            print("Arquivo não encontrado.")
        except ValueError as erro:
            print("Erro:", erro)

        opcao = escolherEntrada()


if __name__ == "__main__":
    main()
