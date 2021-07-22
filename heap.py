from heapq import heappush, heappop, _heappop_max, heapify, _heapify_max, nlargest
"""
heapify methods are used after each insertion/deletion
"""
queue = []

heapify(queue) # for min heap

_heapify_max(queue) # for max heap

heappush(queue, obj) # for pushing object to the heap

heappop(queue) # pop the first element in the queue

nlargest(k, queue) # print the k largest elements in the heap
