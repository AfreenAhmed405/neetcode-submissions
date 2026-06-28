class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build afj list
        # keep track of visited node in DFS path
        # Run DFS for every course to handle disconnected components

        adj = {i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            adj[course].append(preq)
    
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adj[course] == []:
                return True
        
            visited.add(course)

            for preq in adj[course]:
                if not dfs(preq):
                    return False
            
            visited.remove(course)
            adj[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True