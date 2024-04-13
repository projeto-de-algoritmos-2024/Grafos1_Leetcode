import collections

class Cycle:
    def shortestCycle(self, N: int, edges: list[list[int]]) -> int:
        INF = 10 ** 20
        best = INF

        e = collections.defaultdict(list)
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)

        for i in range(N):
            dist = [INF] * N
            dist[i] = 0
                
            q = collections.deque()
            q.append(i)

            while len(q) > 0:
                now = q.popleft()

                for v in e[now]:
                    if dist[now] + 1 < dist[v]:
                        dist[v] = dist[now] + 1
                        q.append(v)
                    else:
                        best = min(best, dist[v] + dist[now] + 1)

        return best if best != INF else -1

# Testes
if __name__ == "__main__":
    cycle = Cycle()
    
    # Teste 1
    N1 = 7
    edges1 = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
    print(cycle.shortestCycle(N1, edges1))  # Saída esperada: 3
    
    # Teste 2
    N2 = 5
    edges2 = [[0,1],[1,2],[2,3],[3,4],[4,0]]
    print(cycle.shortestCycle(N2, edges2))  # Saída esperada: 4
