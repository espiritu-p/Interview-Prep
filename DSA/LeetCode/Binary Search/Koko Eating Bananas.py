class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Binary search approach: O(n log P) time, O(1) space."""

        min_speed = 1
        max_speed = max(piles)

        while min_speed < max_speed:
            hours = 0
            mid_speed = (min_speed + max_speed) // 2

            # Ceiling division counts a partial final hour.
            for pile in piles:
                hours += (pile + mid_speed - 1) // mid_speed

            if hours <= h:
                max_speed = mid_speed
            else:
                min_speed = mid_speed + 1

        return min_speed
