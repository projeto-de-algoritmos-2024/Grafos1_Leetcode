from typing import List

class UF:
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, n):
        while n != self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]
        return n
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        if self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q
        elif self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = root_p
        else:
            self.parent[root_q] = root_p
            self.rank[root_p] += 1
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        uf = UF(n)
        colors = {}  # armazena as cores dos nós
        
        for i in range(n):
            if i not in colors:  # Se o nó não foi colorido ainda, colora-se
                colors[i] = 0  # Define a cor inicial para o nó como 0
                stack = [i]  # Começa uma pilha com o nó i
                
                while stack:
                    node = stack.pop()  # Pega o último nó da pilha
                    for neighbor in graph[node]:  # Para cada vizinho do nó
                        if neighbor not in colors:  # Se o vizinho ainda não foi colorido
                            colors[neighbor] = 1 - colors[node]  # Atribui-se uma cor diferente
                            stack.append(neighbor)  # Adiciona o vizinho à pilha
                        elif colors[neighbor] == colors[node]:  # Se o vizinho tem a mesma cor que o nó atual
                            return False  # O grafo não é bipartido
        return True  # o grafo é bipartido

# Exemplo de uso:
solution = Solution()
graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(solution.isBipartite(graph))  # Deve retornar True
