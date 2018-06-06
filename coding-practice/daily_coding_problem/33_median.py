"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2

"""
from queue import PriorityQueue


def median(stream):
    min_heap = PriorityQueue()
    max_heap = PriorityQueue()
    median = stream[0]
    min_heap.put((median, median))

    print(median)

    for i in range(1, len(stream)):
        num = stream[i]
        if num < median:
            max_heap.put((-num, num))
        else:
            min_heap.put((num, num))
        if abs(min_heap.qsize() - max_heap.qsize()) > 1:
            balance_heaps(min_heap, max_heap)

        median = get_median(min_heap, max_heap)
        print(median)


def balance_heaps(min_heap, max_heap):
    if max_heap.qsize() > min_heap.qsize():
        _, num = max_heap.get()
        min_heap.put((num, num))
    else:
        _, num = min_heap.get()
        max_heap.put((-num, num))


def get_median(min_heap, max_heap):
        median = -1
        # if odd get from large heap
        if (min_heap.qsize() + max_heap.qsize()) % 2 == 0:
            _, min_num = min_heap.get()
            min_heap.put((min_num, min_num))
            _, max_num = max_heap.get()
            max_heap.put((-max_num, max_num))
            median = (min_num + max_num) / 2

        else:  # else get from both and average
            if max_heap.qsize() > min_heap.qsize():
                _, num = max_heap.get()
                max_heap.put((-num, num))
                median = num
            else:
                num, _ = min_heap.get()
                min_heap.put((num, num))
                median = num
        return median


stream = [2, 1, 5, 7, 2, 0, 5]
median(stream)
