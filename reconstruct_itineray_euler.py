from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)

        for departure, destination in tickets:
            graph[departure].append(destination)

        for i in graph.keys():
            graph[i] = sorted(graph[i])
            
        path = []
        print graph
        def DFS(s):
            q = graph.get(s, [])
            while q:
                DFS(q.pop(0)) 
            path.append(s)
            
            
        DFS('JFK')
        return path[::-1]

print(Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))