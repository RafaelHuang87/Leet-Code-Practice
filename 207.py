class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        import collections
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        visited = [0] * numCourses
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, i):
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 2
        return True