import sys

from maze import Maze

ESTILO_CSS = """
  body { font-family: sans-serif; background:#1e1e1e; color:#eee; text-align:center; padding:20px; }
  .labirinto { display:inline-block; border:4px solid #333; }
  .linha { display:flex; }
  .celula { width:18px; height:18px; box-sizing:border-box; }
  .parede { background:#f5c518; }
  .passagem { background:#2b2b2b; }
  .visitado { background:#4da3ff; }
  .entrada { background:#ff4d4d; }
  .saida { background:#3ddc84; }
  .legenda { margin-top:20px; display:flex; justify-content:center; gap:20px; flex-wrap:wrap; }
  .item { display:flex; align-items:center; gap:6px; }
  .caixa { width:16px; height:16px; display:inline-block; }
"""


def descobrirClasseCss(labirinto, numero_da_linha, numero_da_coluna, caractere):
    if numero_da_linha == labirinto.entryCell.x and numero_da_coluna == labirinto.entryCell.y:
        return "entrada"

    if caractere == labirinto.wall:
        return "parede"

    if caractere == labirinto.exitMarker:
        return "saida"

    if caractere == labirinto.visited:
        return "visitado"

    return "passagem"


def montarHtmlDoLabirinto(labirinto):
    html_das_linhas = ""

    numero_da_linha = 0
    while numero_da_linha < len(labirinto.maze):
        linha = labirinto.maze[numero_da_linha]

        html_da_linha = "<div class=\"linha\">"

        numero_da_coluna = 0
        while numero_da_coluna < len(linha):
            caractere = linha[numero_da_coluna]
            classe_css = descobrirClasseCss(labirinto, numero_da_linha, numero_da_coluna, caractere)
            html_da_linha = html_da_linha + "<div class=\"celula " + classe_css + "\"></div>"
            numero_da_coluna = numero_da_coluna + 1

        html_da_linha = html_da_linha + "</div>"

        html_das_linhas = html_das_linhas + html_da_linha + "\n"
        numero_da_linha = numero_da_linha + 1

    return html_das_linhas


def gerarArquivoHtml(labirinto, caminho_do_arquivo_de_saida):
    altura = len(labirinto.maze)
    largura = len(labirinto.maze[0])

    grade_html = montarHtmlDoLabirinto(labirinto)

    conteudo_html = (
        "<!doctype html>\n"
        "<html lang=\"pt-br\">\n"
        "<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<title>Trapped Mouse - Visualizacao</title>\n"
        "<style>" + ESTILO_CSS + "</style>\n"
        "</head>\n"
        "<body>\n"
        "  <h1>Trapped Mouse - Labirinto " + str(largura) + "x" + str(altura) + "</h1>\n"
        "  <div class=\"labirinto\">\n"
        + grade_html +
        "  </div>\n"
        "  <div class=\"legenda\">\n"
        "    <div class=\"item\"><span class=\"caixa parede\"></span> parede (1)</div>\n"
        "    <div class=\"item\"><span class=\"caixa passagem\"></span> corredor nao visitado (0)</div>\n"
        "    <div class=\"item\"><span class=\"caixa visitado\"></span> caminho percorrido (.)</div>\n"
        "    <div class=\"item\"><span class=\"caixa entrada\"></span> entrada do rato (m)</div>\n"
        "    <div class=\"item\"><span class=\"caixa saida\"></span> saida (e)</div>\n"
        "  </div>\n"
        "</body>\n"
        "</html>\n"
    )

    arquivo_de_saida = open(caminho_do_arquivo_de_saida, "w", encoding="utf-8")
    arquivo_de_saida.write(conteudo_html)
    arquivo_de_saida.close()


def lerLinhasDoArquivo(caminho_do_arquivo):
    arquivo = open(caminho_do_arquivo, encoding="utf-8")

    linhas = []
    for linha_bruta in arquivo:
        linha = linha_bruta.rstrip("\n")
        linha = linha.rstrip("\r")
        if linha.strip() != "":
            linhas.append(linha)

    arquivo.close()
    return linhas


def main():
    if len(sys.argv) > 1:
        caminho_do_arquivo_de_entrada = sys.argv[1]
    else:
        caminho_do_arquivo_de_entrada = "entrada3.txt"

    if len(sys.argv) > 2:
        caminho_do_arquivo_de_saida = sys.argv[2]
    else:
        caminho_do_arquivo_de_saida = "visualizacao.html"

    linhas = lerLinhasDoArquivo(caminho_do_arquivo_de_entrada)

    labirinto = Maze(linhas)
    labirinto.exitMaze()

    gerarArquivoHtml(labirinto, caminho_do_arquivo_de_saida)
    print("Visualizacao gerada em " + caminho_do_arquivo_de_saida)


if __name__ == "__main__":
    main()
