# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.


from typing import List
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        distance = [[float("inf")] * n for _ in range(n)]

        for i in range(n):
            distance[i][i] = 0

        for u, v, w in edges:
            distance[u][v] = w
            distance[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distance[i][j] > distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
        
        minReachableCities = float('inf')
        bestCity = -1

        for i in range(n):
            reachableCities = 0
            for j in range(n):
                if distance[i][j] <= distanceThreshold:
                    reachableCities += 1
            
            if reachableCities <= minReachableCities:
                minReachableCities = reachableCities
                bestCity = i
        
        return bestCity