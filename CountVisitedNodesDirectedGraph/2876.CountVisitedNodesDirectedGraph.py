class Solucao:
    def countVisitedNodes(self, arestas):
        n = len(arestas)  # Número de nós no grafo

        visitados = [0] * n  # Estado de visita para cada nó: 0 = não visitado, 1 = visitando, 2 = totalmente visitado
        distancia = [0] * n  # Distância desde o nó inicial até o nó atual na travessia
        contador = [0] * n  # Contador de nós distintos visitados

        for i in range(n):
            if visitados[i] == 0:  # Se o nó ainda não foi visitado, inicie uma nova travessia DFS
                self.dfs(arestas, i, visitados, distancia, contador)
        
        return contador  # Retorna o array com o número de nós visitados para cada nó inicial

    def dfs(self, arestas, i, visitados, distancia, contador):
        visitados[i] = 1  # Marca o nó como sendo visitado

        proximo = arestas[i]  # Obtém o próximo nó no grafo dirigido
        if visitados[proximo] == 0:  # Se o próximo nó não foi visitado
            distancia[proximo] = distancia[i] + 1  # Atualiza a distância para o próximo nó
            contador[proximo] = contador[i] + 1  # Atualiza o contador para o próximo nó
            self.dfs(arestas, proximo, visitados, distancia, contador)  # Continua a DFS a partir do próximo nó

            if distancia[proximo] < distancia[i] + 1:  # Se o próximo nó já estava em um ciclo
                contador[i] = contador[proximo]  # Herda o contador do próximo nó
                distancia[i] = distancia[proximo]  # Garante que o nó atual está no ciclo também
            else:
                contador[i] = contador[proximo] + 1  # Incrementa o contador
        elif visitados[proximo] == 1:  # Se o próximo nó está sendo visitado (ciclo detectado)
            contador[i] = distancia[i] + 1 - distancia[proximo]  # Calcula o número de nós no ciclo
            distancia[i] = distancia[proximo]  # Atualiza a distância para manter a consistência do ciclo
        else:
            contador[i] = contador[proximo] + 1  # Usa o contador do próximo nó e adiciona o nó atual

        visitados[i] = 2  # Marca o nó como totalmente visitado
