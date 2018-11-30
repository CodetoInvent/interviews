# Given an array of meeting time intervals consisting of start and end times 
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.


import heapq

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

times = [Interval(0, 30), Interval(5, 10), Interval(15, 20)] 

def meetings(intervals):
	if not intervals: return 0

	intervals = sorted(intervals, key=lambda x: x.start)

	heap = []
	heapq.heappush(heap, intervals[0].end)

	for i in intervals[1:]:

		peek = heap[0]

		print peek, i.start
		if peek > i.start:
			heapq.heappush(heap, i.end)
		else:
			heapq.heappushpop(heap, i.end)

	return len(heap)

print meetings(times)




