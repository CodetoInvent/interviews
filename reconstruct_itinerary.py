# 332. Reconstruct Itinerary

# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

# Note:

# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# Example 1:

# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:

# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.


itinerary = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]



from collections import defaultdict

def reconstruct_itinerary(itinerary):
	flight_mapping = defaultdict(list)

	for departure, destination in itinerary:
		flight_mapping[departure].append(destination)

	for i in flight_mapping.keys():
		flight_mapping[i] = sorted(flight_mapping[i], reverse=True)


	return traverse_itinerary(flight_mapping, 'JFK', [])



def traverse_itinerary(flight_mapping, departure, itinerary):
	itinerary.append(departure)

	if not departure in flight_mapping: return itinerary

	destination = flight_mapping[departure].pop()
	if not flight_mapping[departure]:
		del flight_mapping[departure]

	return traverse_itinerary(flight_mapping, 
		destination, 
		itinerary
	)



print reconstruct_itinerary(itinerary)