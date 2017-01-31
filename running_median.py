# https://www.hackerrank.com/challenges/ctci-find-the-running-median
from __future__ import division
import heapq


n = [12, 4, 5, 3, 8, 7]

min_heap = []
max_heap = []

bigger = lambda x, y: (x, y) if len(x) >= len(y) else (y, x)


def insert_to_heap(n):
    if (not max_heap) or max_heap[0] > n:
        heapq.heappush(max_heap, n)
    else:
        heapq.heappush(min_heap, n)


def rebalance_heap():
    heapify()
    big, small = bigger(min_heap, max_heap)

    if len(big) - len(small) >= 2:
        y = heapq.heappop(big)
        heapq.heappush(small, y)
        heapify()


def heapify():
    heapq.heapify(min_heap)
    heapq._heapify_max(max_heap)

def median_value():
    if len(min_heap) == len(max_heap):
        mini = min_heap[0]
        maxi = max_heap[0]
        return (mini+maxi)/2

    big, small = bigger(min_heap, max_heap)

    median = big[0]
    return median


for i in n:
    # print min_heap, max_heap
    insert_to_heap(i)
    rebalance_heap()
    print median_value()