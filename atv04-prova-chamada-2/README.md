# Respostas
1. Cada símbolo é processado uma vez e as operações da pilha são O(1), então o tempo é O(n). A pilha pode chegar a n elementos, então a memória é O(n). Na subtração e na divisão desempilho primeiro o b e depois o a, e calculo a - b e a / b.

2. Guardar e retirar são O(1), a memória é fixa em O(capacidade) e nada é deslocado. Para separar cheia de vazia eu guardo também a quantidade de elementos: vazia é quando tamanho é 0 e cheia é quando tamanho é igual à capacidade, mesmo com início e fim na mesma posição. A posição de escrita é (inicio + tamanho) % capacidade.

3. Registrar é O(1), só empilha na pilha de entrada. Informar a quantidade é O(1) com um contador. O próximo pedido só move os pedidos de uma pilha para a outra quando a de saída está vazia. Cada pedido muda de pilha no máximo uma vez, da entrada para a saída, e depois só sai. Então n pedidos custam no máximo n empilhamentos, n transferências e n retiradas, ou seja O(n) para n operações, e O(1) amortizado por operação.

4. a) Uso dois ponteiros, um anda 1 nó e o outro anda 2. Se existir ciclo eles se encontram, se o rápido chegar no fim da lista não tem ciclo. É O(n) de tempo e O(1) de memória. Rota vazia ou com uma parada sem ciclo dá falso.
b) Adianto um ponteiro k nós e depois ando os dois juntos até o da frente chegar na última parada, aí o outro está logo antes da parada a remover. Se o da frente acabar antes de dar k passos, k é maior que a rota e nada muda. Se acabar exatamente após k passos, remove a primeira e devolve inicio.proxima. É O(n) de tempo, uma passada só, e O(1) de memória.

5. Entrar é O(1), consultar a vez é O(1) e eliminar é O(1), porque guardo o nó anterior ao da vez. Avançar k posições é O(k mod n), já que dar voltas completas não muda nada, então um k enorme não trava. A simulação elimina n - 1 jogadores e cada avanço custa até n - 1, então no pior caso é O(n²), contando também a montagem da roda em O(n).

6. Todas as operações são O(1), porque a lista tem inicio e fim e cada nó tem anterior e proximo, então mexo só nas pontas. Quando a fila fica vazia, inicio e fim voltam para None, e com um cliente só inicio e fim apontam para o mesmo nó. Numa lista simples a desistência do último não seria O(1) porque, para o fim passar a ser o penúltimo, eu precisaria chegar nele, e o último nó não aponta para trás, então teria que percorrer a lista toda, que é O(n).
