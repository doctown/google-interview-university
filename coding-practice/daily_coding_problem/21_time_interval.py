"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

Notes:
    Questions: Will the first number always be smaller than the second
    Example: [(90, 91), (91, 100), (4, 5)] = 1
    Brute force: start with each and create all possible combinations
    -   Create a tree with the possible times, and possible next times,
    -   Find the smallest interval and add it if possible until full
    -   Use a priority queue based on end-time
"""


from queue import PriorityQueue


# Time - O(n*log(n)), Space - O(n)
def get_min(intervals):
    intervals.sort()
    pq = PriorityQueue()

    min_num_of_rooms = 2**32

    for start, end in intervals:
        if pq.qsize() == 0:
            pq.put((end, start))
        else:
            meeting_end, meeting_start = pq.get()
            if meeting_end > start:
                pq.put((meeting_end, meeting_start))
            pq.put((end, start))

    min_num_of_rooms = min(min_num_of_rooms, pq.qsize())

    return min_num_of_rooms


def TestSuite():
    intervals = [(30, 75), (0, 50), (60, 150)]
    expected = 2
    actual = get_min(intervals)

    assert expected == actual, "{} == {}".format(expected, actual)

    print("Successfully completed")


if __name__ == "__main__":
    TestSuite()
