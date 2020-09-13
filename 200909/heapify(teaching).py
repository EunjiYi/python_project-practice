def heapify(v):
    if v > n:
        return
    else:

        heapify(v * 2)
        if heap[v] < heap[v//2]:
            heap[v], haap[v//2] = heap[v//2], heap[v]
        heapify(v * 2 + 1)
        if heap[v] < heap[v//2]:
            heap[v], haap[v//2] = heap[v//2], heap[v]
