# Respostas
1. Tempo O(n), cada símbolo é visto uma vez, e memória O(n) pela pilha. Na subtração e na divisão desempilho o b primeiro e depois o a, e faço a - b e a / b

2. Guardar e retirar são O(1) e a memória é fixa. Guardo o tamanho, então vazia é tamanho 0 e cheia é tamanho igual a capacidade, não preciso olhar as posições

3. Registrar é O(1) e o proximo é O(1) amortizado. Cada pedido muda de pilha no máximo uma vez, da entrada pra saída, então n pedidos custam no máximo 3n operações

4. a) Dois ponteiros, um anda 1 e o outro 2, se tiver ciclo eles se encontram. O(n) de tempo e O(1) de memória
b) Adianto um ponteiro k nós e ando os dois juntos até o da frente chegar na última parada. O(n) numa passada só e O(1) de memória

5. Entrar, consultar a vez e eliminar são O(1) e avançar é O(k mod n). A simulação completa é O(n^2) no pior caso

6. Tudo O(1) porque só mexo nas pontas. Na lista simples o último nó não aponta pra trás, então achar o penúltimo ia exigir percorrer tudo, que é O(n)
