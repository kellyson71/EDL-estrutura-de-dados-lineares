import sys

from maze import Maze

CORES_CSS = """
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


def _classeDaCelula(labirinto, x, y, caractere):
    entrada = (labirinto.entryCell.getX(), labirinto.entryCell.getY())

    if (x, y) == entrada:
        return "entrada"
    if caractere == labirinto.wall:
        return "parede"
    if caractere == labirinto.exitMarker:
        return "saida"
    if caractere == labirinto.visited:
        return "visitado"
    return "passagem"


def gerarHtml(labirinto, caminhoSaida="visualizacao.html"):
    linhasHtml = []
    for x, linha in enumerate(labirinto.maze):
        celulas = "".join(
            f'<div class="celula {_classeDaCelula(labirinto, x, y, c)}"></div>'
            for y, c in enumerate(linha)
        )
        linhasHtml.append(f'<div class="linha">{celulas}</div>')

    gridHtml = "\n".join(linhasHtml)
    altura = len(labirinto.maze)
    largura = len(labirinto.maze[0]) if altura else 0

    html = f"""<!doctype html>
<html lang="pt-br">
<head>
<meta charset="utf-8">
<title>Trapped Mouse - Visualizacao</title>
<style>{CORES_CSS}</style>
</head>
<body>
  <h1>Trapped Mouse &mdash; Labirinto {largura}x{altura}</h1>
  <div class="labirinto">
{gridHtml}
  </div>
  <div class="legenda">
    <div class="item"><span class="caixa parede"></span> parede (1)</div>
    <div class="item"><span class="caixa passagem"></span> corredor nao visitado (0)</div>
    <div class="item"><span class="caixa visitado"></span> caminho percorrido (.)</div>
    <div class="item"><span class="caixa entrada"></span> entrada do rato (m)</div>
    <div class="item"><span class="caixa saida"></span> saida (e)</div>
  </div>
</body>
</html>
"""

    with open(caminhoSaida, "w", encoding="utf-8") as arquivo:
        arquivo.write(html)

    return caminhoSaida


def main():
    caminhoEntrada = sys.argv[1] if len(sys.argv) > 1 else "entrada3.txt"
    caminhoSaida = sys.argv[2] if len(sys.argv) > 2 else "visualizacao.html"

    with open(caminhoEntrada, encoding="utf-8") as arquivo:
        linhas = [linha.rstrip("\n").rstrip("\r") for linha in arquivo if linha.strip() != ""]

    labirinto = Maze(linhas)
    labirinto.exitMaze()

    caminhoGerado = gerarHtml(labirinto, caminhoSaida)
    print(f"Visualizacao gerada em {caminhoGerado}")


if __name__ == "__main__":
    main()
