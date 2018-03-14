"""
    You run a sneaker website and want to record the last N order ids in a log.
    Implement a data structure to accomplish this, with the following API:

    • record(order_id): adds the order_id to the log
    • get_last(i): gets the ith last element from the log.
      - i is guaranteed to be smaller than or equal to N.
"""


class log:
    def __init__(self):
        # self.heap = Heap()
        self.items = []

    def record(self, order_id):
        #  adds the order_id to the log
        # self.heap.insert(order_id)
        self.items.append(order_id)

    def get_last(i): # gets the ith last element from the log.
        if i >= len(self.items):
            raise ValueError('i is larger than items recorded')
        #ith = None
        #elements =[self.heap.getMax() for _ in range(i)]

        #ith = elements.pop()
        #[ self.heap.insert(elem) for elem in elements]

        #return ith
        return self.items[i]
# create a max heap, store the items in the max heap based on id

# get items from the up to i and then reinsert them at the end
