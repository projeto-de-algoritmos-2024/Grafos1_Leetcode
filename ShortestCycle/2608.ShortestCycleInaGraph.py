import collections
from typing import List

class Solution:
    def findShortestCycle(self, N: int, edges: List[List[int]]) -> int:
        INF = 10 ** 20
        best = INF
        
        e = collections.defaultdict(list)
        # Preenche a lista de adjacência com as arestas fornecidas
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)

        # Itera sobre cada nó no grafo
        for i in range(N):
            # Inicializa uma lista para armazenar a distância do nó atual para todos os outros nós
            dist = [INF] * N
            # Define a distância do nó atual para si mesmo como 0
            dist[i] = 0
                
            # Inicializa uma fila para a BFS e enfileira o nó atual
            q = collections.deque()
            q.append(i)

            # Inicializa uma lista para armazenar o pai de cada nó na árvore BFS
            parents =[-1] * N

            # Realiza a BFS
            while len(q) > 0:
                now = q.popleft()  # Desenfileira um nó da fila

                # Itera sobre os vizinhos do nó desenfileirado
                for v in e[now]:
                    # Se a distância até o vizinho pode ser reduzida passando pelo nó desenfileirado
                    if dist[now] + 1 < dist[v]:
                        # Atualiza a distância e o pai do vizinho
                        dist[v] = dist[now] + 1
                        parents[v] = now
                        # Enfileira o vizinho para exploração adicional
                        q.append(v)
                    # Se o vizinho não é o pai do nó desenfileirado e vice-versa
                    else:
                        # Verifica se um ciclo é encontrado e atualiza o comprimento do ciclo mais curto, se necessário
                        if parents[v] != now and parents[now] != v:
                            best = min(best, dist[v] + dist[now] + 1)

        # Se nenhum ciclo for encontrado, retorna -1
        if best >= INF: 
            return -1
        
        # Caso contrário, retorna o comprimento do ciclo mais curto
        return best

# Casos de teste
n = 7
arestas = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]
sol = Solution()
resultado = sol.findShortestCycle(n, arestas)
print("Saída:", resultado)

n2 = 4
arestas2 = [[0,1],[0,2]]
sol2 = Solution()
resultado2 = sol2.findShortestCycle(n2, arestas2)
print("Saída:", resultado2)
