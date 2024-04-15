class Solution:
    def countPairs(self, N: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(N)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            ux = find(x)
            uy = find(y)

            parent[ux] = uy 

        for u, v in edges:
            union(u, v)
        
        count = collections.Counter()
        for i in range(N):
            count[find(i)] += 1

        total = 0
        for k, v in count.items():
            total += count[k] * (N - count[k])
        return total // 2


        