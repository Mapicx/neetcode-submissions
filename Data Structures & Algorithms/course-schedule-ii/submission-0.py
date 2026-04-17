class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        res = []
        cycle = set()
        visit = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in premap[crs]:
                if dfs(pre) == False:
                    return False
            visit.add(crs)
            premap[crs] = []
            cycle.remove(crs)
            res.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res


            

        