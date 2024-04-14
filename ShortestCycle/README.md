
# 2608. Shortest Cycle in a Graph

Existe um gráfico bidirecional com nvértices, onde cada vértice é rotulado de 0até n - 1. As arestas no gráfico são representadas por um determinado array inteiro 2D edges, onde denota uma aresta entre vértice e vértice . Cada par de vértices é conectado por no máximo uma aresta, e nenhum vértice possui uma aresta própria.edges[i] = [ui, vi]uivi

Retorne a duração do ciclo mais curto do gráfico . Se não existir nenhum ciclo, retorne -1.

Um ciclo é um caminho que começa e termina no mesmo nó, e cada aresta do caminho é usada apenas uma vez.

## Exemplo 1:

![](https://github.com/projeto-de-algoritmos-2024/Grafos1_Leetcode/blob/main/assets/exemplo1.png)<br>
```

 Entrada: n = 7, arestas = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3] ]

 Saída: 3
 
 Explicação: O ciclo com o menor comprimento é: 0 -> 1 -> 2 -> 0 
```

## Exemplo 2:

![](https://github.com/projeto-de-algoritmos-2024/Grafos1_Leetcode/blob/main/assets/exemplo2.png)<br>
```

 Entrada: n = 4, arestas = [[0,1],[0,2]]

 Saída: -1
 
 Explicação: Não há ciclos neste gráfico.
```

## Restrições:

• 2 <= n <= 1000
• 1 <= edges.length <= 1000
• edges[i].length == 2
• 0 <= ui, vi < n
• ui != vi
• Não há arestas repetidas.