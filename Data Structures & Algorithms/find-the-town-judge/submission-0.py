class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mapping = {}
        for i in range(1, n + 1):
            mapping[i] = {"indegree": 0, "outdegree": 0}
        res = []
        for src, dst in trust:
            mapping[src]["outdegree"] += 1
            mapping[dst]["indegree"] += 1
        for i in range(1, n+1):
            if mapping[i]["indegree"] == n - 1 and mapping[i]["outdegree"] == 0:
                res.append(i)
        if len(res) == 1:
            return res[0]
        return -1 
        
        