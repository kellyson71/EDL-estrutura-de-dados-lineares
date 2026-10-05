import os

CAMINHO_DESTE_ARQUIVO = os.path.abspath(__file__)
PASTA = os.path.dirname(CAMINHO_DESTE_ARQUIVO)
CARACTERES_VALIDOS = "01me"


def validarLabirinto(linhas):
    if len(linhas) == 0:
        raise ValueError("Nenhum labirinto encontrado.")

    largura = len(linhas[0])
    quantidadeRatos = 0
    quantidadeSaidas = 0

    for linha in linhas:
        if len(linha) != largura:
            raise ValueError("Todas as linhas precisam ter o mesmo tamanho.")

        for caractere in linha:
            if caractere not in CARACTERES_VALIDOS:
                raise ValueError("Caractere inválido: " + caractere)
            if caractere == "m":
                quantidadeRatos += 1
            if caractere == "e":
                quantidadeSaidas += 1

    if quantidadeRatos != 1 or quantidadeSaidas != 1:
        raise ValueError("Cada labirinto precisa ter exatamente um 'm' e um 'e'.")


def lerLabirintosDoArquivo(nomeArquivo):
    caminho = os.path.join(PASTA, nomeArquivo)
    labirintos = []
    labirintoAtual = []

    with open(caminho, encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if linha != "":
                labirintoAtual.append(linha)
            elif len(labirintoAtual) > 0:
                labirintos.append(labirintoAtual)
                labirintoAtual = []

    if len(labirintoAtual) > 0:
        labirintos.append(labirintoAtual)

    if len(labirintos) == 0:
        raise ValueError("Nenhum labirinto encontrado.")

    for labirinto in labirintos:
        validarLabirinto(labirinto)

    return labirintos


def lerLabirintoDoTeclado():
    print("Digite o labirinto, uma linha por vez.")
    print("Use 0 (corredor), 1 (parede), m (rato) e e (saída).")
    print("Para terminar, aperte ENTER em uma linha vazia.")

    linhas = []
    linha = input().strip()
    while linha != "":
        linhas.append(linha)
        linha = input().strip()

    validarLabirinto(linhas)
    return linhas
