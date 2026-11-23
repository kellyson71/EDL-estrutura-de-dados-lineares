# Respostas
Questão 1. O tempo é O(n), porque cada símbolo é visto uma vez, e a memória é O(n) pela pilha. Na subtração e na divisão desempilho o b primeiro e depois o a, e calculo a - b e a / b.

Questão 2. Guardar e retirar são O(1) e a memória é fixa. Eu guardo a quantidade de elementos, então vazia é tamanho 0 e cheia é tamanho igual à capacidade, mesmo com início e fim na mesma posição.

Questão 3. Registrar é O(1) e obter o próximo é O(1) amortizado. Cada pedido muda de pilha no máximo uma vez, da entrada para a saída, então n pedidos custam no máximo 3n operações.

Questão 4. a) Dois ponteiros, um andando 1 e outro 2, que se encontram se houver ciclo, em O(n) de tempo e O(1) de memória. b) Adianto um ponteiro k nós e ando os dois juntos até o da frente chegar na última parada, em O(n) numa passada só e O(1) de memória.

Questão 5. Entrar, consultar a vez e eliminar são O(1), e avançar é O(k mod n). A simulação completa é O(n²) no pior caso.

Questão 6. Todas as operações são O(1) porque mexo só nas pontas da lista. Numa lista simples o último nó não aponta para trás, então achar o penúltimo exigiria percorrer tudo, que é O(n).
