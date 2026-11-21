#ifndef PILHA_HPP
#define PILHA_HPP

#include <stdexcept>

template <typename K, typename V>
class Pilha {
    struct No {
        K chave;
        V valor;
        No* abaixo;
        No(const K& c, const V& v, No* a) : chave(c), valor(v), abaixo(a) {}
    };

    No* topo = nullptr;
    int tamanho = 0;

public:
    Pilha() = default;
    Pilha(const Pilha&) = delete;
    Pilha& operator=(const Pilha&) = delete;
    ~Pilha() { while (!vazia()) desempilhar(); }

    void empilhar(const K& chave, const V& valor) {
        topo = new No(chave, valor, topo);
        tamanho++;
    }

    void desempilhar() {
        if (vazia()) throw std::underflow_error("pilha vazia");
        No* velho = topo;
        topo = topo->abaixo;
        delete velho;
        tamanho--;
    }

    K& chaveTopo() {
        if (vazia()) throw std::underflow_error("pilha vazia");
        return topo->chave;
    }

    V& valorTopo() {
        if (vazia()) throw std::underflow_error("pilha vazia");
        return topo->valor;
    }

    bool vazia() const { return topo == nullptr; }
    int size() const { return tamanho; }
};

#endif
