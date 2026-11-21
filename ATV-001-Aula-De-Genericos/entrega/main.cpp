#include <iostream>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <utility>

#include "fila.hpp"
#include "lista.hpp"
#include "pilha.hpp"

using namespace std;

int main() {
    cout << "Pilha<int, string> x stack<pair<int, string>>\n";
    Pilha<int, string> pilha;
    stack<pair<int, string>> pilhaStd;
    string nomes[] = {"ana", "bruno", "carla"};
    for (int i = 0; i < 3; i++) {
        pilha.empilhar(i + 1, nomes[i]);
        pilhaStd.push({i + 1, nomes[i]});
    }
    while (!pilha.vazia()) {
        cout << "  minha: " << pilha.chaveTopo() << " " << pilha.valorTopo()
             << " | std: " << pilhaStd.top().first << " " << pilhaStd.top().second << "\n";
        pilha.desempilhar();
        pilhaStd.pop();
    }

    cout << "\nFila<string, double> x queue<pair<string, double>>\n";
    Fila<string, double> fila;
    queue<pair<string, double>> filaStd;
    string itens[] = {"cafe", "pao", "leite"};
    double precos[] = {8.5, 1.25, 5.0};
    for (int i = 0; i < 3; i++) {
        fila.enfileirar(itens[i], precos[i]);
        filaStd.push({itens[i], precos[i]});
    }
    while (!fila.vazia()) {
        cout << "  minha: " << fila.chaveFrente() << " " << fila.valorFrente()
             << " | std: " << filaStd.front().first << " " << filaStd.front().second << "\n";
        fila.desenfileirar();
        filaStd.pop();
    }

    cout << "\nLista<char, int> x list<pair<char, int>>\n";
    Lista<char, int> lista;
    list<pair<char, int>> listaStd;
    lista.inserirFim('b', 2);
    lista.inserirFim('c', 3);
    lista.inserirInicio('a', 1);
    listaStd.push_back({'b', 2});
    listaStd.push_back({'c', 3});
    listaStd.push_front({'a', 1});

    cout << "  minha:";
    lista.percorrer([](char c, int v) { cout << " (" << c << "," << v << ")"; });
    cout << "\n  std:  ";
    for (auto& p : listaStd) cout << " (" << p.first << "," << p.second << ")";
    cout << "\n";

    lista.remover('b');
    listaStd.remove_if([](const pair<char, int>& p) { return p.first == 'b'; });
    cout << "  depois de remover 'b': minha=" << lista.size() << " std=" << listaStd.size() << "\n";
    cout << "  contem 'a': " << lista.contem('a') << ", contem 'b': " << lista.contem('b') << "\n";

    try {
        Pilha<int, int> vazia;
        vazia.desempilhar();
    } catch (const underflow_error& e) {
        cout << "\nerro esperado: " << e.what() << "\n";
    }
    return 0;
}
