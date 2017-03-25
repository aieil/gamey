import heapq

class PQ(object):
    """Priority queue."""
    def __init__(self):
        self.Q = []
        self.length = 0

    def push(self, item, priority = 0):
        heapq.heappush(self.Q, (priority, item))
        self.length += 1

    def isEmpty(self):
        return self.length == 0

    def __str__(self):
        return str(self.Q)

    def pop(self):
        try:
            return heapq.heappop(self.Q)
            self.length -= 1
        except IndexError as e:
            # this would mean that there is no solution to the problem.
            print("The PQ is empty. There is no solution")
            raise
