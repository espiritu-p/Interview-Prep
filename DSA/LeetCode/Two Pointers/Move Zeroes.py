class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
            1. The plan
            - The simpler solution is to just write the non-zero elements in the first elements of the array in order and fill the remaining with zeroes
            - what we can do is to have a pointer set at 0 which moves everytime we move a non-zero number
            2. Time/Space Complexity
            - Time Complexity: O(n)
            - Space Complexity: O(1)
        """
        ptr = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[ptr] = nums[i]
                ptr += 1

        for i in range(ptr, len(nums)):
            nums[i] = 0
