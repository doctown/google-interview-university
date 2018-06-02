"""

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.


No clear plan



              #
              #
#        #    #
#        #    #
#  _  #  # _  #
1) get depth from left and right walls, record min height
2) move rigth or left wall inward, whichever is smaller -
3) compare
   - if next wall is smaller or equal to min_height, decrement water level by wall height, move again
   - set new boundary, compare to other wall,
        - if both larger than min, add depth, update min
        - update min
"""


def trapped_water(walls):
    if len(walls) == 0:
        return 0

    units_of_water = 0
    left_boundary = 0
    right_boundary = len(walls) - 1
    min_height = 0

    while left_boundary < right_boundary:
        left_height = walls[left_boundary]
        right_height = walls[right_boundary]

        min_boundary_height = min(left_height, right_height)

        if left_height <= min_height or right_height <= min_height:
            units_of_water += min_height - min_boundary_height
        elif left_height > min_height and right_height > min_height:
            min_height = min_boundary_height

        if left_height < right_height:
            left_boundary += 1
        else:
            right_boundary -= 1

    return units_of_water


def TestSuite():
    walls = [2, 1, 2]
    output = 1
    actual = trapped_water(walls)

    assert actual == output, "{} == {}".format(actual, output)

    walls = [3, 0, 1, 3, 0, 5]
    output = 8
    actual = trapped_water(walls)

    assert actual == output, "{} == {}".format(actual, output)

    print("Done")


TestSuite()
