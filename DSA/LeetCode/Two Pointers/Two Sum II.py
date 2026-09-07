class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        1. Problem
            - Find two integers where the two numbers when summed will be equal to the target number.
              Array is already in non-decreasing order so we might be able to take advantage of this setup.
        2. Plan
            - O(n^2) solution where I'd just check each two number combination in the array and sum it
            - O(n)/O(1) we can shorten the solution space by adjusting the left and right pointers
              using the following conditions:
                - left + right > target
                    - we can adjust the right -= 1 to get a lower sum
                    - safe because numbers[left] is the SMALLEST available partner for numbers[right];
                      if even it overshoots, no pair using numbers[right] can work — discard right
                      eliminates only provably-invalid pairs
                - left + right < target
                    - we can adjust the left += 1 to get a higher sum (mirror argument)
                - since there's always a solution per input array, return the indices of left and
                  right that matches the target when summed (1-indexed per the problem)
            - Variants not written: binary search per element O(n log n)/O(1) — dominated by the
              two-pointer since both ends move; hash map O(n)/O(n) — ignores the sortedness.
        3. Time/Space Complexity
            - Time Complexity: O(n)
            - Space Complexity: O(1)
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current = numbers[left] + numbers[right]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            else:
                return [left + 1, right + 1]
