class Solucao:
    def countVisitedNodes(self, arestas):
        n = len(arestas)

        visitados = [0] * n
        distancia = [0] * n
        contador = [0] * n

        for i in range(n):
            if visitados[i] == 0:
                self.dfs(arestas, i, visitados, distancia, contador)
        
        return contador

    def dfs(self, arestas, i, visitados, distancia, contador):
        visitados[i] = 1

        proximo = arestas[i]
        if visitados[proximo] == 0:
            distancia[proximo] = distancia[i] + 1
            contador[proximo] = contador[i] + 1
            self.dfs(arestas, proximo, visitados, distancia, contador)

            if distancia[proximo] < distancia[i] + 1:
                contador[i] = contador[proximo]
                distancia[i] = distancia[proximo]   #ter certeza que continua no ciclo
            else:
                contador[i] = contador[proximo] + 1
        elif visitados[proximo] == 1:
            contador[i] = distancia[i] + 1 - distancia[proximo]
            distancia[i] = distancia[proximo] #ter certeza que continua no ciclo
        else:
            contador[i] = contador[proximo] + 1

        visitados[i] = 2
