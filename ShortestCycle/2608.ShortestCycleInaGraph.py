import collections
from typing import List

class Solution:
    def findShortestCycle(self, N: int, edges: List[List[int]]) -> int:
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

            parents =[-1] * N

            while len(q) > 0:
                now = q.popleft()

                for v in e[now]:
                    if dist[now] + 1 < dist[v]:
                        dist[v] = dist[now] + 1
                        parents[v] = now
                        q.append(v)
                    else:
                        if parents[v] != now and parents[now] != v:
                            best = min(best, dist[v] + dist[now] + 1)

        if best >= INF: 
            return -1
        
        return best
    
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
