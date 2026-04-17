class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for src, dst in prerequisites:
            graph[src].append(dst)
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if graph[course] == []:
                return True
            
            visit.add(course)
            for nei in graph[course]:
                if dfs(nei) == False:
                    return False
            visit.remove(course)
            graph[course] = []
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True