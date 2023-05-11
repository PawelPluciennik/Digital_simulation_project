class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, element):
        self._queue.append(element)
        return self

    def dequeue(self):
        return self._queue.pop()

    def __len__(self):
        return len(self._queue)
