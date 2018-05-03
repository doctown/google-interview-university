import math


def create_tree(nums):
    result = []
    queue = [nums]

    while len(queue) != 0:
        elem = queue.pop()
        if len(elem):
            mid_idx = math.floor(len(elem) / 2)
            print(mid_idx)
            result.append(elem[mid_idx])
            print(elem[:mid_idx])
            queue.append(elem[:mid_idx])
            print(elem[mid_idx + 1:])
            queue.append(elem[mid_idx + 1:])

    return result


nums = [1, 2, 3, 10, 17, 20]
print(create_tree(nums))
