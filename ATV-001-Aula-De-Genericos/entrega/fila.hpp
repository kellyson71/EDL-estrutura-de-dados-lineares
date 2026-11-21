#ifndef FILA_HPP
#define FILA_HPP

#include <stdexcept>

template <typename K, typename V>
class Fila {
    struct No {
        K chave;
        V valor;
        No* proximo = nullptr;
        No(const K& c, const V& v) : chave(c), valor(v) {}
    };

    No* inicio = nullptr;
    No* fim = nullptr;
    int tamanho = 0;

public:
    Fila() = default;
    Fila(const Fila&) = delete;
    Fila& operator=(const Fila&) = delete;
    ~Fila() { while (!vazia()) desenfileirar(); }

    void enfileirar(const K& chave, const V& valor) {
        No* novo = new No(chave, valor);
        if (fim) fim->proximo = novo;
        else inicio = novo;
        fim = novo;
        tamanho++;
    }

    void desenfileirar() {
        if (vazia()) throw std::underflow_error("fila vazia");
        No* velho = inicio;
        inicio = inicio->proximo;
        if (!inicio) fim = nullptr;
        delete velho;
        tamanho--;
    }

    K& chaveFrente() {
        if (vazia()) throw std::underflow_error("fila vazia");
        return inicio->chave;
    }

    V& valorFrente() {
        if (vazia()) throw std::underflow_error("fila vazia");
        return inicio->valor;
    }

    bool vazia() const { return inicio == nullptr; }
    int size() const { return tamanho; }
};

#endif
