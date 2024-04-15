from typing import List

class UF:
    
    def __init__(self, n):
        self.parent = list(range(n)) #inicializa, cada nó cé seu proprio pai
        self.rank = [1] * n #inicialmente com 1 
        
    def find(self, n):
        while n != self.parent[n]: # enquanto não for a raiz do conjunto
            self.parent[n] = self.parent[self.parent[n]] # define o pai do nó como avo, e reduz a altura da arvore
            n = self.parent[n] # atualiza
        return n # retorna a raiz
    
    def union(self, p, q):
        root_p = self.find(p) #encontra a raiz do conjunto ao qual o elemento p pertence
        root_q = self.find(q)
        if root_p == root_q: # verifica se já pertence ao mesmo conjunto
            return
        if self.rank[root_p] < self.rank[root_q]: # se o conjunto p for menor que q
            self.parent[root_p] = root_q # une 
        else: # se os conjuntos forem iguais 
            self.parent[root_q] = root_p # une
            self.rank[root_p] += 1 #incrementa a p
    
    def connected(self, p, q):
        return self.find(p) == self.find(q) # verifca se ambos estão no mesmo conjunto
    
    
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph) # número de nós
        uf = UF(n) 
        colors = {}  # armazena as cores dos nós
        
        for i in range(n):
            if i not in colors:  # se o nó não foi colorido ainda, colora-se
                colors[i] = 0  
                stack = [i]  # começa uma pilha com o nó i
                
                while stack:
                    node = stack.pop()  # pega o último nó da pilha
                    for neighbor in graph[node]:  # para cada vizinho do nó
                        if neighbor not in colors:  # se o vizinho ainda não foi colorido
                            colors[neighbor] = 1 - colors[node]  # coloere uma cor diferente
                            stack.append(neighbor)  # adiciona o vizinho à pilha
                        elif colors[neighbor] == colors[node]:  # se o vizinho tem a mesma cor que o nó atual
                            return False  # O grafo não é bipartido
        return True  # o grafo é bipartido

# Exemplo de uso:
solution = Solution()
graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(solution.isBipartite(graph))  # Deve retornar True
