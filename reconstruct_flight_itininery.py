from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        return reconstruct_itinerary(tickets)

def reconstruct_itinerary(itinerary):
    flight_mapping = defaultdict(list)

    for departure, destination in itinerary:
        flight_mapping[departure].append(destination)

    for i in flight_mapping.keys():
        flight_mapping[i] = sorted(flight_mapping[i])
        
    print(flight_mapping)
    return traverse_itinerary(flight_mapping, 'JFK', [])



def traverse_itinerary(flight_mapping, departure, itinerary):
    itinerary.append(departure)

    if not departure in flight_mapping: return itinerary

    print flight_mapping[departure]
    destination = flight_mapping[departure].pop()
    if not flight_mapping[departure]:
        del flight_mapping[departure]

    return traverse_itinerary(flight_mapping, 
        destination, 
        itinerary
    )



print(Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))


# from collections import defaultdict
# class Solution(object):
#     def findItinerary(self, tickets):
#         """
#         :type tickets: List[List[str]]
#         :rtype: List[str]
#         """
#         graph, path = {}, []
#         for ticket in tickets:
#             graph[ticket[0]] = graph.get(ticket[0], []) + [ticket[1]]
#         print graph
#         for key in graph.keys():
#             graph[key].sort()
            
#         def DFS(s):
#             q = graph.get(s, [])
#             while q:
#                 DFS(q.pop(0)) 
#             path.append(s)
            
#         DFS('JFK')
#         return path[::-1]