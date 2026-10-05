import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox

from maze import Maze

PASTA_DO_PROGRAMA = os.path.dirname(os.path.abspath(__file__))
CARACTERES_VALIDOS = "01me"
DELAY = 0.08


def validarLabirinto(labirinto):
    largura = len(labirinto[0])
    quantidadeRatos = 0
    quantidadeSaidas = 0

    for linha in labirinto:
        if len(linha) != largura:
            raise ValueError("Todas as linhas precisam ter o mesmo tamanho.")
        for caractere in linha:
            if caractere not in CARACTERES_VALIDOS:
                raise ValueError("Caractere inválido: " + caractere)
        quantidadeRatos += linha.count("m")
        quantidadeSaidas += linha.count("e")

    if quantidadeRatos != 1 or quantidadeSaidas != 1:
        raise ValueError("Cada labirinto precisa ter exatamente um 'm' e um 'e'.")


def lerLabirintos(texto):
    labirintos = []
    labirintoAtual = []

    for linha in texto.splitlines():
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


def ehTextoDeLabirinto(texto):
    if texto.strip() == "":
        return False
    for caractere in texto:
        if caractere not in CARACTERES_VALIDOS and not caractere.isspace():
            return False
    return True


class Interface:
    def __init__(self, janela):
        self.janela = janela
        self.labirintos = []
        self.indice = 0
        self.resolvendo = False

        janela.title("Trapped Mouse")
        janela.geometry("720x640")

        linhaArquivo = tk.Frame(janela, padx=10, pady=5)
        linhaArquivo.pack(fill="x")
        tk.Label(linhaArquivo, text="Arquivo:").pack(side="left")
        self.campoCaminho = tk.Entry(linhaArquivo, width=30)
        self.campoCaminho.insert(0, "entrada_multipla.txt")
        self.campoCaminho.pack(side="left", padx=5)
        self.campoCaminho.bind("<Return>", lambda evento: self.carregarArquivo())
        tk.Button(linhaArquivo, text="Carregar", command=self.carregarArquivo).pack(side="left")
        tk.Button(linhaArquivo, text="Buscar...", command=self.buscarArquivo).pack(side="left", padx=5)

        linhaAcoes = tk.Frame(janela, padx=10, pady=5)
        linhaAcoes.pack(fill="x")
        tk.Button(linhaAcoes, text="Novo Texto", command=self.novoTexto).pack(side="left")
        tk.Button(linhaAcoes, text="Editar Texto", command=self.editarTexto).pack(side="left", padx=5)
        tk.Button(linhaAcoes, text="◀", command=lambda: self.navegar(-1)).pack(side="left", padx=5)
        self.rotuloContador = tk.Label(linhaAcoes, width=18, font=("Arial", 10, "bold"))
        self.rotuloContador.pack(side="left")
        tk.Button(linhaAcoes, text="▶", command=lambda: self.navegar(1)).pack(side="left", padx=5)
        tk.Button(linhaAcoes, text="Resolver", command=self.resolver).pack(side="left", padx=10)

        self.areaTexto = tk.Text(janela, font=("Courier", 13), wrap="none")
        self.areaTexto.pack(fill="both", expand=True, padx=10)

        self.rotuloStatus = tk.Label(janela, anchor="w", padx=10, pady=5)
        self.rotuloStatus.pack(fill="x")

        self.novoTexto()

    def escreverNaTela(self, texto):
        self.areaTexto.delete("1.0", tk.END)
        self.areaTexto.insert("1.0", texto)

    def atualizarContador(self):
        total = len(self.labirintos)
        if total == 0:
            self.rotuloContador.config(text="Nenhum labirinto")
        else:
            self.rotuloContador.config(text="Labirinto " + str(self.indice + 1) + " de " + str(total))

    def definirLabirintos(self, labirintos):
        self.labirintos = labirintos
        self.indice = 0
        self.mostrarAtual()

    def mostrarAtual(self):
        self.atualizarContador()
        self.escreverNaTela(str(Maze(self.labirintos[self.indice])))
        self.rotuloStatus.config(text="Pronto para resolver.")

    def carregarArquivo(self):
        caminho = self.campoCaminho.get().strip()
        if not os.path.exists(caminho):
            caminho = os.path.join(PASTA_DO_PROGRAMA, caminho)

        try:
            with open(caminho, encoding="utf-8") as arquivo:
                self.definirLabirintos(lerLabirintos(arquivo.read()))
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo não encontrado: " + self.campoCaminho.get())
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def buscarArquivo(self):
        caminho = filedialog.askopenfilename(initialdir=PASTA_DO_PROGRAMA, filetypes=[("Texto", "*.txt")])
        if caminho != "":
            self.campoCaminho.delete(0, tk.END)
            self.campoCaminho.insert(0, caminho)
            self.carregarArquivo()

    def novoTexto(self):
        if self.resolvendo:
            return
        self.labirintos = []
        self.atualizarContador()
        self.escreverNaTela("")
        self.rotuloStatus.config(text="Digite os labirintos (0, 1, m, e). Separe vários com uma linha vazia.")
        self.areaTexto.focus_set()

    def editarTexto(self):
        if self.resolvendo or len(self.labirintos) == 0:
            return
        blocos = []
        for labirinto in self.labirintos:
            blocos.append("\n".join(labirinto))
        self.escreverNaTela("\n\n".join(blocos))
        self.rotuloStatus.config(text="Edite o texto e clique em Resolver.")

    def navegar(self, passo):
        if self.resolvendo or len(self.labirintos) == 0:
            return
        self.indice = (self.indice + passo) % len(self.labirintos)
        self.mostrarAtual()

    def resolver(self):
        if self.resolvendo:
            return

        texto = self.areaTexto.get("1.0", tk.END)
        if ehTextoDeLabirinto(texto):
            try:
                self.definirLabirintos(lerLabirintos(texto))
            except ValueError as erro:
                messagebox.showerror("Erro", str(erro))
                return

        if len(self.labirintos) == 0:
            messagebox.showwarning("Aviso", "Digite um labirinto ou carregue um arquivo.")
            return

        maze = Maze(self.labirintos[self.indice])

        def mostrarPasso():
            self.escreverNaTela(str(maze))
            self.janela.update()
            time.sleep(DELAY)

        self.resolvendo = True
        self.rotuloStatus.config(text="Procurando a saída...")
        try:
            encontrou = maze.exitMaze(mostrarPasso)
        except tk.TclError:
            return
        self.resolvendo = False

        if encontrou:
            self.rotuloStatus.config(text="Saída encontrada!")
        else:
            self.rotuloStatus.config(text="Caminho não encontrado!")


if __name__ == "__main__":
    janela = tk.Tk()
    Interface(janela)
    janela.mainloop()
