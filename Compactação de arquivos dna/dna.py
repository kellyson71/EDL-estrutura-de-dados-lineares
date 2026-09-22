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
    binario = bin(compactado)
    binario = binario[2:]
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

    with open(caminho, "w") as arquivo:
        arquivo.write(str(tamanho) + "\n")
        arquivo.write(bits)


def abrir_compactado(caminho):
    with open(caminho, "r") as arquivo:
        tamanho = int(arquivo.readline())
        bits = arquivo.readline()

    compactado = int(bits, 2)

    return compactado, tamanho


pasta = os.path.dirname(os.path.abspath(__file__))
arquivoEntrada = os.path.join(pasta, "dna.txt")
arquivoCompactado = os.path.join(pasta, "dna_compactado.txt")

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

if compactado == None:
    print("Não foi possível compactar.")

else:
    salvar_compactado(arquivoCompactado, compactado, tamanho)
    print()

    print("DNA original:")
    print(dna)

    print()

    bitsOriginal = tamanho * 8

    print("Tamanho original:")
    print(bitsOriginal, "bits")

    print()

    binarioCompactado = mostrar_binario(compactado, tamanho)

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

    compactadoLido, tamanhoLido = abrir_compactado(arquivoCompactado)
    dnaDescompactado = descompactar(compactadoLido, tamanhoLido)

    print("DNA descompactado:")
    print(dnaDescompactado)

    if dna == dnaDescompactado:
        print("Descompactação feita corretamente.")
    else:
        print("Alguma coisa deu errado.")