#ifndef LISTA_HPP
#define LISTA_HPP

#include <stdexcept>

template <typename K, typename V>
class Lista {
    struct No {
        K chave;
        V valor;
        No* anterior = nullptr;
        No* proximo = nullptr;
        No(const K& c, const V& v) : chave(c), valor(v) {}
    };

    No* inicio = nullptr;
    No* fim = nullptr;
    int tamanho = 0;

    No* buscar(const K& chave) const {
        for (No* p = inicio; p; p = p->proximo)
            if (p->chave == chave) return p;
        return nullptr;
    }

public:
    Lista() = default;
    Lista(const Lista&) = delete;
    Lista& operator=(const Lista&) = delete;
    ~Lista() { while (inicio) removerInicio(); }

    void inserirInicio(const K& chave, const V& valor) {
        No* novo = new No(chave, valor);
        novo->proximo = inicio;
        if (inicio) inicio->anterior = novo;
        else fim = novo;
        inicio = novo;
        tamanho++;
    }

    void inserirFim(const K& chave, const V& valor) {
        No* novo = new No(chave, valor);
        novo->anterior = fim;
        if (fim) fim->proximo = novo;
        else inicio = novo;
        fim = novo;
        tamanho++;
    }

    void removerInicio() {
        if (!inicio) throw std::underflow_error("lista vazia");
        No* velho = inicio;
        inicio = inicio->proximo;
        if (inicio) inicio->anterior = nullptr;
        else fim = nullptr;
        delete velho;
        tamanho--;
    }

    void removerFim() {
        if (!fim) throw std::underflow_error("lista vazia");
        No* velho = fim;
        fim = fim->anterior;
        if (fim) fim->proximo = nullptr;
        else inicio = nullptr;
        delete velho;
        tamanho--;
    }

    bool remover(const K& chave) {
        No* p = buscar(chave);
        if (!p) return false;
        if (p->anterior) p->anterior->proximo = p->proximo;
        else inicio = p->proximo;
        if (p->proximo) p->proximo->anterior = p->anterior;
        else fim = p->anterior;
        delete p;
        tamanho--;
        return true;
    }

    V* get(const K& chave) {
        No* p = buscar(chave);
        return p ? &p->valor : nullptr;
    }

    bool contem(const K& chave) const { return buscar(chave) != nullptr; }
    bool vazia() const { return inicio == nullptr; }
    int size() const { return tamanho; }

    template <typename F>
    void percorrer(F f) const {
        for (No* p = inicio; p; p = p->proximo) f(p->chave, p->valor);
    }
};

#endif
