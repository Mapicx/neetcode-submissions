class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if graph[crs] == []:
                return True
            visit.add(crs)
            for pre in graph[crs]:
                if dfs(pre) == False:
                    return False
            graph[crs] = []
            visit.remove(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True


        