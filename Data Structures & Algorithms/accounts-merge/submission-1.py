class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(list)
        emailToName = {}

        # Build graph
        for account in accounts:
            name = account[0]

            for email in account[1:]:
                emailToName[email] = name

            for i in range(2, len(account)):
                email1 = account[i]
                email2 = account[i - 1]

                adj[email1].append(email2)
                adj[email2].append(email1)

        # DFS
        visited = set()
        res = []

        def dfs(email, emails):
            visited.add(email)
            emails.append(email)

            for nei in adj[email]:
                if nei not in visited:
                    dfs(nei, emails)

        # Find connected components
        for email in emailToName:
            if email not in visited:
                emails = []
                dfs(email, emails)

                name = emailToName[email]
                res.append([name] + sorted(emails))

        return res