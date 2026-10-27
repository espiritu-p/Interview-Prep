class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Problem: Find the largest area formed by two vertical lines and the x-axis.
        Edge cases: Two lines; equal heights; zero heights. Empty and single-element
            inputs return 0, though LeetCode requires at least two lines.
        Plan: Start at both ends, track the largest area, and move the shorter line.
            Keeping it cannot improve the area because every remaining width is smaller.
        Complexity: O(n) time, O(1) extra space.
        Variant: Check every pair in O(n^2) time and O(1) extra space.
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            left_height = height[left]
            right_height = height[right]
            area = min(left_height, right_height) * (right - left)
            max_area = max(max_area, area)

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return max_area
