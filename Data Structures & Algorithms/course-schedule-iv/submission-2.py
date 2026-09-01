class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:

        graph = [[] for _ in range(numCourses)]

        for pre, crs in prerequisites:
            graph[pre].append(crs)

        reachable = [[False] * numCourses for _ in range(numCourses)]

        def dfs(src, node):
            for nei in graph[node]:
                if not reachable[src][nei]:
                    reachable[src][nei] = True
                    dfs(src, nei)

        for i in range(numCourses):
            dfs(i, i)

        return [reachable[pre][crs] for pre, crs in queries]