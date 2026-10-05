import os
import sys


def compactar(dna):
    compactado = 0

    for letra in dna:
        compactado = compactado << 2

        if letra == "A":
            valor = 0
        elif letra == "C":
            valor = 1
        elif letra == "G":
            valor = 2
        elif letra == "T":
            valor = 3
        else:
            print("Letra inválida encontrada:", letra)
            return None

        compactado = compactado | valor

    return compactado


def descompactar(compactado, tamanho):
    dna = ""
    numero = compactado
    contador = 0

    while contador < tamanho:
        valor = numero & 3

        if valor == 0:
            letra = "A"
        elif valor == 1:
            letra = "C"
        elif valor == 2:
            letra = "G"
        else:
            letra = "T"

        dna = letra + dna
        numero = numero >> 2
        contador = contador + 1

    return dna


def mostrar_binario(compactado, tamanho):
    binario = bin(compactado)[2:]
    quantidadeBits = tamanho * 2

    while len(binario) < quantidadeBits:
        binario = "0" + binario

    return binario


def ler_dna(caminho):
    with open(caminho, "r") as arquivo:
        texto = arquivo.read()

    return "".join(texto.split()).upper()


def salvar_compactado(caminho, compactado, tamanho):
    bits = mostrar_binario(compactado, tamanho)

    while len(bits) % 8 != 0:
        bits = "0" + bits

    dados = int(bits, 2).to_bytes(
        len(bits) // 8,
        byteorder="big"
    )

    with open(caminho, "wb") as arquivo:
        arquivo.write(tamanho.to_bytes(4, byteorder="big"))
        arquivo.write(dados)


def abrir_compactado(caminho):
    with open(caminho, "rb") as arquivo:
        tamanho = int.from_bytes(
            arquivo.read(4),
            byteorder="big"
        )

        dados = arquivo.read()

    compactado = int.from_bytes(
        dados,
        byteorder="big"
    )

    return compactado, tamanho


pasta = os.path.dirname(os.path.abspath(__file__))
arquivoEntrada = os.path.join(pasta, "dna.txt")
arquivoCompactado = os.path.join(pasta, "dna_compactado.bin")

print("COMPACTAÇÃO DE DNA")

try:
    dna = ler_dna(arquivoEntrada)
except FileNotFoundError:
    print("Arquivo não encontrado:", arquivoEntrada)
    sys.exit(1)

tamanho = len(dna)

if tamanho == 0:
    print("O arquivo está vazio.")
    sys.exit(1)

compactado = compactar(dna)

if compactado is None:
    print("Não foi possível compactar.")
else:
    salvar_compactado(
        arquivoCompactado,
        compactado,
        tamanho
    )

    print()
    print("DNA original:")
    print(dna)

    print()

    bitsOriginal = tamanho * 8

    print("Tamanho original:")
    print(bitsOriginal, "bits")

    print()

    binarioCompactado = mostrar_binario(
        compactado,
        tamanho
    )

    print("DNA compactado em bits:")
    print(binarioCompactado)

    bitsCompactados = tamanho * 2

    print("Tamanho compactado:")
    print(bitsCompactados, "bits")

    print()

    bitsEconomizados = bitsOriginal - bitsCompactados

    porcentagem = bitsEconomizados / bitsOriginal
    porcentagem = porcentagem * 100

    print("Bits economizados:")
    print(bitsEconomizados, "bits")

    print("Economia:")
    print(porcentagem, "%")

    print()

    compactadoLido, tamanhoLido = abrir_compactado(
        arquivoCompactado
    )

    dnaDescompactado = descompactar(
        compactadoLido,
        tamanhoLido
    )

    print("DNA descompactado:")
    print(dnaDescompactado)

    if dna == dnaDescompactado:
        print("Descompactação feita corretamente.")
    else:
        print("Alguma coisa deu errado.")