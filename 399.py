class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        import collections
        def dfs(x, y, graph, visited):
            if x not in graph or y not in graph:
                return -1
            if x == y:  return 1

            for n in graph[x]:
                if n in visited:
                    continue
                visited.add(n)
                d = dfs(n, y, graph, visited)
                if d != -1:
                    return graph[x][n] * d
            return -1

        graph = collections.defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val

        return [dfs(x, y, graph, set()) for x, y in queries]
