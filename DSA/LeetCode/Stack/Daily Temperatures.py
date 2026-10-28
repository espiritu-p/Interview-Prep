class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Problem: Find the number of days until a strictly warmer temperature.
        Edge cases: Equal or decreasing temperatures; no warmer day; one day.
        Plan: Store unresolved indices in a non-increasing temperature stack.
            A warmer day resolves colder days from the top; record the distance.
            Unresolved days keep zero.
        Complexity: O(n) time: each index is pushed once and popped at most once.
            O(n) auxiliary space for the stack, excluding the O(n) output.
        Variant: Search forward for each day in O(n^2) time, O(1) auxiliary space.
        """
        n = len(temperatures)
        stack = []
        ans = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                previous_day = stack.pop()
                ans[previous_day] = i - previous_day
            stack.append(i)

        return ans


if __name__ == "__main__":
    solution = Solution()
    for temperatures, expected in (
        ([], []),
        ([70], [0]),
        ([70, 70, 70], [0, 0, 0]),
        ([75, 74, 73], [0, 0, 0]),
        ([70, 71, 72], [1, 1, 0]),
        ([73, 71, 70, 72], [0, 2, 1, 0]),
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ):
        assert solution.dailyTemperatures(temperatures) == expected, temperatures
