"""
    Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

    Given nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
    It doesn't matter what you leave beyond the new length.
"""

"""
    Notes:
    brute-force: sort array and shift left when duplicate found. Then traverse array and move to first position
"""

# O(n)
class Solution:
    def removeDuplicates(self, nums):
        """
            :type nums: List[int]
            :rtype: int
        """
        if len(nums) == 0:
            return 0

        nums.sort()

        uniq_col = 1

        # [1, 1, 2]
        for idx in range(1, len(nums)):
            cur_num = nums[idx]
            neighbor = nums[idx - 1]

            if cur_num != neighbor:
                nums[uniq_col] = cur_num
                uniq_col += 1

        return nums[:uniq_col]

    def testSuite(self):
        nums = [1, 2, 1]
        output = 2
        actual = self.removeDuplicates(nums)

        assert actual == output, "{} == {}".format(actual, output)

        nums = [1, 1, 1]
        output = 1
        actual = self.removeDuplicates(nums)

        assert actual == output, "{} == {}".format(actual, output)

        nums = [1]
        output = 1
        actual = self.removeDuplicates(nums)

        assert actual == output, "{} == {}".format(actual, output)

        nums = []
        output = 0
        actual = self.removeDuplicates(nums)

        assert actual == output, "{} == {}".format(actual, output)


        print("Successfully tested")


sol = Solution()
sol.testSuite()

